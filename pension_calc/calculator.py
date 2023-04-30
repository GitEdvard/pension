import datetime
from pension_calc.config import open_config

class Calculator:
    def __init__(self):
        self.config = open_config()
        today = datetime.date.today()
        current_year = today.year
        self.year_to_pension = 1971 + self.config.age_of_pension - current_year

    def accomodation_cost(self):
        monthly_interest = self.config.loan_size * self.config.interest_current / 100 / 12 * 0.7
        monthly_interest_gross = monthly_interest / 0.7
        monthly_fee = self.config.monthly_fee
        amortalization = self.config.amortalization
        monthly_cost = monthly_interest + monthly_fee
        monthly_payment = monthly_interest_gross + monthly_fee + amortalization
        return monthly_interest, monthly_fee, amortalization, monthly_cost, monthly_payment
