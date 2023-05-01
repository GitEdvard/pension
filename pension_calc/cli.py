import click
from pension_calc.calculator import Calculator

@click.group()
@click.option('--whatif/--not-whatif', default=False)
@click.pass_context
def cli(ctx, whatif):
    ctx.obj['whatif'] = whatif


@cli.command("accomodation")
@click.pass_context
def accomodation(ctx):
    calculator = Calculator()
    monthly_interest, monthly_fee, amortalization, monthly_cost, monthly_payment = \
        calculator.accomodation_cost()
    print("Current interest: {:.1f}%".format(calculator.config.interest_current))
    print("Monthly interest (interest deduction): {} kr".format(fmt(monthly_interest)))
    print("monthly_fee: {} kr".format(fmt(monthly_fee)))
    print("Amortalization: {} kr".format(fmt(amortalization)))
    print("Interest and fee (interest deduction): {} kr".format(fmt(monthly_cost)))
    print("Monthly gross payment, (amortalization and no interest deduction): {} kr".format(fmt(monthly_payment)))


@cli.command("growth")
@click.pass_context
def growth(ctx):
    calculator = Calculator()
    annual_growth, savings, savings_at_pension = \
        calculator.return_on_savings()
    print("Annual growth: {:.1f}%".format(annual_growth))
    print("Initial savings: {} kr".format(fmt(savings)))
    print("Age of pension: {}".format(fmt(calculator.config.age_of_pension)))
    print("Savings at pension: {} kr".format(fmt(savings_at_pension)))



@cli.command("pension_payment")
@click.pass_context
def pension_payment(ctx):
    calculator = Calculator()
    pension_tax, pension_gross, pension_net = calculator.pension_payment()
    print("Pension tax: {:.1f}%".format(pension_tax))
    print("Gross pension: {} kr".format(fmt(pension_gross)))
    print("Net pension: {} kr".format(fmt(pension_net)))


def fmt(amount):
    fmt_amount = "{:,.0f}".format(amount)
    new_amount = fmt_amount.replace(",", " ")
    return new_amount


def cli_main():
    cli(obj={})


if __name__ == "__main__":
    cli_main()
