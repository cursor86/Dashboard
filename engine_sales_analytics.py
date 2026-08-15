from factory_lib import compile_template, buyer_env

if __name__ == "__main__":
    buyer_name, buyer_niche, currency = buyer_env()
    compile_template("sales_analytics_template.xlsx", "Custom_Sales_Analytics", buyer_name, buyer_niche, currency)
