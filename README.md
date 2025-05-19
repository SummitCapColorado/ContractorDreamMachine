
# PassiveCashflowBot

## Overview
This repo contains everything needed to auto‑generate a daily micro‑product (PDF) and push it to Gumroad via Zapier.

- `generate_product.py`: Python script called by Zapier each night.
- `config.yaml`: Place your API keys and Gumroad IDs here.
- `placeholder.pdf`: Dummy file to upload to Gumroad before automation starts.

## Quick Start
1. Fork/clone this repo into your GitHub account (public or private).
2. Fill in `config.yaml`.
3. Import the provided `.zap` files into Zapier, update connections.
