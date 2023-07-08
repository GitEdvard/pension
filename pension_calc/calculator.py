import datetime
import math
from pension_calc.config import CONFIG
from pension_calc.dto.accomodation import Accomodation
from pension_calc.dto.growth import Growth
from pension_calc.dto.pension_payment import PensionPayment
from pension_calc.dto.accomodation_pension import AccomodationPension
from pension_calc.dto.balance import Balance

class Calculator:
    def __init__(self):
        self.config = CONFIG
        today = datetime.date.today()
        current_year = today.year
        self.year_to_pension = 1971 + self.config.age_of_pension - current_year
        self.number_months = self.year_to_pension * 12

    def accomodation_cost_now(self):
        a = Accomodation()
        a.monthly_interest = self.config.loan_size * self.config.interest_current / 100 / 12 * 0.7
        monthly_interest_gross = a.monthly_interest / 0.7
        a.monthly_fee = self.config.monthly_fee
        a.amortalization = self.config.amortalization
        a.monthly_cost = a.monthly_interest + a.monthly_fee
        a.monthly_payment = monthly_interest_gross + a.monthly_fee + a.amortalization
        a.interest_current = self.config.interest_current
        return a

    def accomodation_cost_pension(self):
        a = AccomodationPension()
        a.interest_pension = self.config.interest_pension
        a.inflation = self.config.inflation
        a.amortalization = self.config.amortalization
        a.loan_size = self.config.loan_size
        a.loan_at_pension_amo_only = a.loan_size - a.amortalization * self.number_months
        r = 1 - a.inflation / 100
        a.loan_after_inflation_no_amo = \
                a.loan_size * math.pow(r, self.year_to_pension)
        # Calculate with geometric series on amortalization due to inflation
        a.loan_at_pension = a.loan_after_inflation_no_amo - a.amortalization * 12 \
                * (1 - math.pow(r, self.year_to_pension)) / (1 - r)
        a.monthly_fee = self.config.monthly_fee
        a.monthly_cost = a.monthly_fee * 1.15 \
                + a.loan_at_pension * a.interest_pension / 100 / 12 * 0.7
        return a

    def pension_payment(self):
        p = PensionPayment()
        p.pension_net = self.config.pension_gross * (1 - self.config.pension_tax / 100)
        p.pension_tax = self.config.pension_tax
        p.pension_gross = self.config.pension_gross
        p.age_of_death = self.config.age_of_death
        g = self.return_on_savings()
        number_years = p.age_of_death - self.config.age_of_pension
        p.monthly_payment_from_savings = g.savings_at_pension / number_years / 12
        return p

    def balance(self):
        b = Balance()
        b.expenses_apart_from_accomodation = self.config.expenses_apart_from_accomodation
        p = self.pension_payment()
        b.income = p.pension_net + p.monthly_payment_from_savings
        a = self.accomodation_cost_pension()
        b.rent = a.monthly_cost
        b.balance = b.income - b.expenses_apart_from_accomodation - b.rent
        return b

    def return_on_savings(self):
        g = Growth()
        g.savings = self.config.savings
        g.annual_growth = self.config.annual_growth
        g.return_on_initial = g.savings * math.pow ((1 + g.annual_growth/100), self.year_to_pension)
        monthly_saving = self.config.monthly_saving
        monthly_growth = g.annual_growth / 12
        g.total_monthly_payment = monthly_saving * self.number_months
        r = 1 + monthly_growth/100
        # geometric series
        g.return_from_monthly = monthly_saving * (1 - math.pow(r, self.number_months)) / (1 - r)
        g.savings_at_pension = g.return_from_monthly + g.return_on_initial
        g.age_of_pension = self.config.age_of_pension
        g.monthly_saving = self.config.monthly_saving
        return g
