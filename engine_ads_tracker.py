from factory_lib import compile_template, buyer_env

if __name__ == "__main__":
    buyer_name, buyer_niche, currency = buyer_env()
    compile_template("social_ads_tracker_template.xlsx", "Custom_Social_Ads_Tracker", buyer_name, buyer_niche, currency)
