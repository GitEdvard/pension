class Presenter:
    @staticmethod
    def accomodation_now(a):
        print("Current interest: {:.1f}%".format(a.interest_current))
        print("Monthly interest (interest deduction): {} kr".format(fmt(a.monthly_interest)))
        print("monthly_fee: {} kr".format(fmt(a.monthly_fee)))
        print("Amortalization: {} kr".format(fmt(a.amortalization)))
        print("Interest and fee (interest deduction): {} kr".format(fmt(a.monthly_cost)))
        print("Monthly gross payment, (amortalization and no interest deduction): {} kr" \
                .format(fmt(a.monthly_payment)))

    @staticmethod
    def accomodation_pension(a):
        print("Annual inlation: {}%".format(a.inflation))
        print("Interest at pension: {}%".format(a.interest_pension))
        print("Monthly amortalization: {} kr".format(fmt(a.amortalization)))
        print("Current loan size: {} kr".format(fmt(a.loan_size)))
        print("Loan at pension acconting only amortalization: {} kr"\
                .format(fmt(a.loan_at_pension_amo_only)))
        print("Loan at pension acconting for inflation only {} kr"\
                .format(fmt(a.loan_after_inflation_no_amo)))
        print("Loan at pension acconting both inflation and amortalization: {} kr"\
                .format(fmt(a.loan_at_pension)))
        print("Monthly cost for accomodation at pension (fee + interest with deduction): {} kr" \
                .format(fmt(a.monthly_cost)))

    @staticmethod
    def balance(b):
        print("Income after pension (pension + savings): {} kr".format(fmt(b.income)))
        print("Accomondation cost after pension: {} kr".format(fmt(b.rent)))
        print("Expenses after pension, apart from accomodation: {} kr". \
                format(fmt(b.expenses_apart_from_accomodation)))
        print("Monthly balance: {} kr".format(fmt(b.balance)))

    @staticmethod
    def growth(g):
        print("Annual growth: {:.1f}%".format(g.annual_growth))
        print("Initial savings: {} kr".format(fmt(g.savings)))
        print("Age of pension: {}".format(fmt(g.age_of_pension)))
        print("Monthly saving rate: {} kr".format(fmt(g.monthly_saving)))
        print("Total monthly payment at pension: {} kr".format(fmt(g.total_monthly_payment)))
        print("Return on monthly savings at pension: {} kr".format(fmt(g.return_from_monthly)))
        print("Return on initial savings at pension: {} kr".format(fmt(g.return_on_initial)))
        print("Savings at pension: {} kr".format(fmt(g.savings_at_pension)))

    @staticmethod
    def payment(p):
        print("Pension tax: {:.1f}%".format(p.pension_tax))
        print("Gross pension: {} kr".format(fmt(p.pension_gross)))
        print("Net pension: {} kr".format(fmt(p.pension_net)))
        print("Age of death: {}".format(p.age_of_death))
        print("Monthly payment from savings: {} kr".format(fmt(p.monthly_payment_from_savings)))
        print("Total monthly payment: {} kr".format(fmt(p.monthly_payment_from_savings + p.pension_net)))


def fmt(amount):
    fmt_amount = "{:,.0f}".format(amount)
    new_amount = fmt_amount.replace(",", " ")
    return new_amount
