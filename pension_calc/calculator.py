import datetime
import math
from pension_calc.config import open_config
from pension_calc.dto.accomodation import Accomodation
from pension_calc.dto.growth import Growth
from pension_calc.dto.pension_payment import PensionPayment

class Calculator:
    def __init__(self):
        self.config = open_config()
        today = datetime.date.today()
        current_year = today.year
        self.year_to_pension = 1971 + self.config.age_of_pension - current_year

    def accomodation_cost(self):
        a = Accomodation()
        a.monthly_interest = self.config.loan_size * self.config.interest_current / 100 / 12 * 0.7
        monthly_interest_gross = a.monthly_interest / 0.7
        a.monthly_fee = self.config.monthly_fee
        a.amortalization = self.config.amortalization
        a.monthly_cost = a.monthly_interest + a.monthly_fee
        a.monthly_payment = monthly_interest_gross + a.monthly_fee + a.amortalization
        return a

    def pension_payment(self):
        p = PensionPayment()
        p.pension_net = self.config.pension_gross * (1 - self.config.pension_tax / 100)
        p.pension_tax = self.config.pension_tax
        p.pension_gross = self.config.pension_gross
        return p

    def return_on_savings(self):
        g = Growth()
        g.savings = self.config.savings
        g.annual_growth = self.config.annual_growth
        g.return_on_initial = g.savings * math.pow ((1 + g.annual_growth/100), self.year_to_pension)
        monthly_saving = self.config.monthly_saving
        monthly_growth = g.annual_growth / 12
        number_months = self.year_to_pension * 12
        g.total_monthly_payment = monthly_saving * number_months
        r = 1 + monthly_growth/100
        # geometric series
        g.return_from_monthly = monthly_saving * (1 - math.pow(r, number_months)) / (1 - r)
        g.savings_at_pension = g.return_from_monthly + g.return_on_initial
        return g
