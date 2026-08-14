import os
import sys
from openpyxl import load_workbook

def run_factory():
    master_file = "master_template.xlsx"

    if not os.path.exists(master_file):
        print(f"❌ Structural Error: '{master_file}' layout blueprint missing.")
        sys.exit(1)

    # Extract order configurations straight from cloud workflow environmental data
    buyer_name = os.getenv("BUYER_NAME", "Valued Client")
    buyer_niche = os.getenv("BUYER_NICHE", "Small Business")
    currency = os.getenv("CURRENCY", "$")

    workbook = load_workbook(master_file)

    # Process matrix parsing loops safely across all sheet tabs
    for sheet in workbook.worksheets:
        for row in sheet.iter_rows(values_only=False):
            for cell in row:
                if cell.value and isinstance(cell.value, str):
                    if "{{CLIENT_NAME}}" in cell.value:
                        cell.value = cell.value.replace("{{CLIENT_NAME}}", buyer_name)
                    if "{{NICHE}}" in cell.value:
                        cell.value = cell.value.replace("{{NICHE}}", buyer_niche)
                    if "{{CURRENCY}}" in cell.value:
                        cell.value = cell.value.replace("{{CURRENCY}}", currency)

    # Save output into a customized client-ready spreadsheet file
    clean_title = buyer_name.replace(" ", "_")
    output_name = f"Custom_Financial_Dashboard_{clean_title}.xlsx"
    workbook.save(output_name)
    print(f"✨ Custom file cleanly generated: {output_name}")

if __name__ == "__main__":
    run_factory()
