
import os, json, datetime, requests, base64, yaml
from fpdf import FPDF

CONFIG = yaml.safe_load(open("config.yaml"))
key = CONFIG["openai"]["OPENAI_API_KEY"]
today = datetime.date.today().strftime("%B %d, %Y")
prompt = f"Generate a JSON list of 20 short actionable marketing ideas for contractors, dated {today}."

resp = requests.post(
    "https://api.openai.com/v1/chat/completions",
    headers={"Authorization": f"Bearer {key}"},
    json={
        "model": "gpt-4o-mini",
        "messages":[{"role":"user","content":prompt}],
        "response_format":{"type":"json_object"}
    }
)
ideas = json.loads(resp.json()["choices"][0]["message"]["content"])["ideas"]

pdf_text = "\n\n".join([f"{i+1}. {idea}" for i, idea in enumerate(ideas)])
pdf = FPDF(); pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page(); pdf.set_font("Arial", size=12)
for line in pdf_text.splitlines():
    pdf.multi_cell(0, 8, line)
filename = "daily_product.pdf"
pdf.output(filename)
print("PDF generated:", filename)
