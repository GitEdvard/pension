import os
import yaml

def open_config():
    here = os.path.dirname(__file__)
    path = os.path.join(here, '/home/edvard/sources/real/pension/resources/data.yml')
    with open(path, 'r') as file:
        config_dict = yaml.load(file, Loader=yaml.FullLoader)
    config = Config(config_dict)
    return config


class Config:
    def __init__(self, config_dict):
        self.savings = config_dict["savings"]
        self.age_of_pension = config_dict["age_of_pension"]
        self.annual_growth = config_dict["annual_growth"]
        self.amortalization = config_dict["amortalization"]
        self.monthly_fee = config_dict["monthly_fee"]
        self.interest_current = config_dict["interest_current"]
        self.loan_size = config_dict["loan_size"]
        self.pension_gross = config_dict["pension_gross"]
        self.pension_tax = config_dict["pension_tax"]
        self.monthly_saving = config_dict["monthly_saving"]
