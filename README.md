# Dashboard: Business Template & Automation Factory

A one-click system that **personalises ready-to-use Excel templates** for each buyer, plus PowerPoint brand kit templates and ready-made **n8n automation workflows** for small businesses, sellers and creators.

Instead of editing every template by hand for each customer, you fill in a short form on GitHub (business name, niche, currency). Python then fills those details into every template and the finished files are ready to download.

![Python](https://img.shields.io/badge/Python-3-3776AB) ![Excel](https://img.shields.io/badge/Excel-openpyxl-217346) ![PowerPoint](https://img.shields.io/badge/PowerPoint-templates-B7472A) ![GitHub Actions](https://img.shields.io/badge/CI-GitHub_Actions-2088FF) ![n8n](https://img.shields.io/badge/Automation-n8n-EA4B71)

---

## What's included

**Spreadsheet templates (Excel, personalised per buyer)**
- Small business bookkeeping
- Bill calendar
- Sales analytics dashboard
- Social media ads tracker
- Pricing calculator
- Small business tracker
- Gym membership tracker
- Master template

**Brand kits (PowerPoint, ready-made templates)**
- eCommerce, Etsy seller and social media creator brand kits, with placeholder text for the buyer to replace

**Automation workflows (n8n)**
- Etsy order automation
- Order status email automation
- Social media auto-poster

## How it works

1. Each master Excel template contains placeholder tags: `{{CLIENT_NAME}}`, `{{NICHE}}` and `{{CURRENCY}}`.
2. In the **Actions** tab you run a workflow (for example "1-Click Etsy Dashboard Engine") and enter the buyer's details.
3. GitHub Actions runs a Python engine that opens each template with **openpyxl**, replaces the tags in every cell and saves a copy named for the buyer.
4. The personalised files are uploaded as a downloadable artifact.

```
factory_lib.py              shared helper: load a template, replace the tags, save
engine.py                   personalises the main set (5 templates)
engine_sales_analytics.py   personalises the sales analytics dashboard
engine_ads_tracker.py       personalises the social ads tracker
engine_gym_tracker.py       personalises the gym membership tracker
.github/workflows/          the 1-click forms that run each engine
n8n_*.json                  importable n8n workflow definitions
```

## Run locally

```bash
pip install openpyxl
BUYER_NAME="Bella's Bakery" BUYER_NICHE="Home baking" CURRENCY="A$" python engine.py
```

## How this was built

Built by **Rizz** using AI-assisted development (Claude Code). My role: product selection, template design from a finance perspective (what small businesses actually need to track), testing and packaging.
