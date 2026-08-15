from factory_lib import compile_template, buyer_env

# Each bundle item is a (blueprint file, output label) pair. Add a new tuple
# here whenever a new bundle workbook (e.g. Small Business Tracker, Bill
# Calendar, Pricing Calculator) gets its own master template file.
TEMPLATES = [
    ("master_template.xlsx", "Custom_Financial_Dashboard"),
    ("bookkeeping_template.xlsx", "Custom_Bookkeeping"),
    ("small_business_tracker_template.xlsx", "Custom_Small_Business_Tracker"),
    ("pricing_calculator_template.xlsx", "Custom_Pricing_Calculator"),
    ("bill_calendar_template.xlsx", "Custom_Bill_Calendar"),
]

def run_factory():
    buyer_name, buyer_niche, currency = buyer_env()
    for master_file, output_label in TEMPLATES:
        compile_template(master_file, output_label, buyer_name, buyer_niche, currency)

if __name__ == "__main__":
    run_factory()
