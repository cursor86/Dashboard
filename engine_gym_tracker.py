from factory_lib import compile_template, buyer_env

if __name__ == "__main__":
    buyer_name, buyer_niche, currency = buyer_env()
    compile_template("gym_membership_tracker_template.xlsx", "Custom_Gym_Membership_Tracker", buyer_name, buyer_niche, currency)
