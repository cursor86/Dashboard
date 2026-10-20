# Dashboard: Business Template & Automation Factory

Python generators that produce ready-to-use **spreadsheet dashboards and business templates** for small businesses, sellers and creators, plus ready-made **n8n automation workflows**.

Instead of hand-building each spreadsheet, every product is generated from code, so the templates are consistent and can be rebuilt or updated in seconds.

![Python](https://img.shields.io/badge/Python-3-3776AB) ![Excel](https://img.shields.io/badge/Excel-openpyxl-217346) ![PowerPoint](https://img.shields.io/badge/PowerPoint-python--pptx-B7472A) ![GitHub Actions](https://img.shields.io/badge/CI-GitHub_Actions-2088FF) ![n8n](https://img.shields.io/badge/Automation-n8n-EA4B71)

---

## What it produces

**Spreadsheet templates (Excel)**
- Small business bookkeeping
- Bill calendar
- Sales analytics dashboard
- Social media ads tracker
- Pricing calculator
- Small business tracker
- Gym membership tracker
- Master template

**Brand kits (PowerPoint)**
- eCommerce, Etsy seller and social media creator brand kits

**Automation workflows (n8n)**
- Etsy order automation
- Order status email automation
- Social media auto-poster

## How it works

```
factory_lib.py              shared styling, formulas and layout helpers
engine.py                   core generator for the main template set
engine_sales_analytics.py   sales analytics dashboard generator
engine_ads_tracker.py       social ads tracker generator
engine_gym_tracker.py       gym membership tracker generator
.github/workflows/          GitHub Actions jobs that rebuild each product line
n8n_*.json                  importable n8n workflow definitions
```

Each product line has its own GitHub Actions workflow, so templates are rebuilt the same way every time.

## Run locally

```bash
pip install openpyxl python-pptx
python engine.py
```

## How this was built

Built by **Rizz** using AI-assisted development (Claude Code). My role: product selection, template design from a finance perspective (what small businesses actually need to track), testing and packaging.
