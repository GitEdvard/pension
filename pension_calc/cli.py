import click
from pension_calc.calculator import Calculator

@click.group()
@click.option('--whatif/--not-whatif', default=False)
@click.pass_context
def cli(ctx, whatif):
    ctx.obj['whatif'] = whatif


@cli.command("calculate")
@click.pass_context
def calculate(ctx):
    calculator = Calculator()
    print(f"savings: {calculator.config.savings} kr")
    print(f"year to pension: {calculator.year_to_pension}")


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

def fmt(amount):
    fmt_amount = "{:,.0f}".format(amount)
    new_amount = fmt_amount.replace(",", " ")
    return new_amount


def cli_main():
    cli(obj={})


if __name__ == "__main__":
    cli_main()
