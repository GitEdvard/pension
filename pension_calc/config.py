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
        self.interest_pension = config_dict["interest_pension"]
        self.inflation = config_dict["inflation"]
        self.loan_size = config_dict["loan_size"]
        self.pension_gross = config_dict["pension_gross"]
        self.pension_tax = config_dict["pension_tax"]
        self.monthly_saving = config_dict["monthly_saving"]
        self.age_of_death = config_dict["age_of_death"]
        self.expenses_apart_from_accomodation= config_dict["expenses_apart_from_accomodation"]

    def __repr__(self):
        info = [
            self.fmt_currency(self.savings, "savings"),
            self.fmt_years(self.age_of_pension, "age_of_pension"),
            self.fmt_percent(self.annual_growth, "annual_growth"),
            self.fmt_currency(self.amortalization, "amortalization"),
            self.fmt_currency(self.monthly_fee, "monthly_fee"),
            self.fmt_percent(self.interest_current, "interest_current"),
            self.fmt_percent(self.interest_pension, "interest_pension"),
            self.fmt_percent(self.inflation, "inflation"),
            self.fmt_currency(self.loan_size, "loan_size"),
            self.fmt_currency(self.pension_gross, "pension_gross"),
            self.fmt_percent(self.pension_tax, "pension_tax"),
            self.fmt_currency(self.monthly_saving, "monthly_saving"),
            self.fmt_years(self.age_of_death, "age_of_death"),
            self.fmt_currency(self.expenses_apart_from_accomodation, "expenses_apart_from_accomodation"),
        ]
        return "\n".join(info)

    @staticmethod
    def fmt_currency(value, name):
        fmt_amount = "{:,.0f}".format(value)
        new_amount = fmt_amount.replace(",", " ")
        return f"{name}: {new_amount} kr"

    @staticmethod
    def fmt_percent(value, name):
        fmt_amount = "{:,.1f}".format(value)
        return f"{name}: {fmt_amount}%"

    @staticmethod
    def fmt_years(value, name):
        fmt_amount = "{:,.0f}".format(value)
        return f"{name}: {fmt_amount} years"


CONFIG = open_config()
