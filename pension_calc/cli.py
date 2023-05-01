from os import walk
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
    a = calculator.accomodation_cost()
    print("Current interest: {:.1f}%".format(calculator.config.interest_current))
    print("Monthly interest (interest deduction): {} kr".format(fmt(a.monthly_interest)))
    print("monthly_fee: {} kr".format(fmt(a.monthly_fee)))
    print("Amortalization: {} kr".format(fmt(a.amortalization)))
    print("Interest and fee (interest deduction): {} kr".format(fmt(a.monthly_cost)))
    print("Monthly gross payment, (amortalization and no interest deduction): {} kr" \
            .format(fmt(a.monthly_payment)))


@cli.command("growth")
@click.pass_context
def growth(ctx):
    calculator = Calculator()
    g = calculator.return_on_savings()
    print("Annual growth: {:.1f}%".format(g.annual_growth))
    print("Initial savings: {} kr".format(fmt(g.savings)))
    print("Age of pension: {}".format(fmt(calculator.config.age_of_pension)))
    print("Monthly saving rate: {} kr".format(fmt(calculator.config.monthly_saving)))
    print("Total monthly payment at pension: {} kr".format(fmt(g.total_monthly_payment)))
    print("Return on monthly savings at pension: {} kr".format(fmt(g.return_from_monthly)))
    print("Return on initial savings at pension: {} kr".format(fmt(g.return_on_initial)))
    print("Savings at pension: {} kr".format(fmt(g.savings_at_pension)))



@cli.command("pension_payment")
@click.pass_context
def pension_payment(ctx):
    calculator = Calculator()
    p = calculator.pension_payment()
    print("Pension tax: {:.1f}%".format(p.pension_tax))
    print("Gross pension: {} kr".format(fmt(p.pension_gross)))
    print("Net pension: {} kr".format(fmt(p.pension_net)))


def fmt(amount):
    fmt_amount = "{:,.0f}".format(amount)
    new_amount = fmt_amount.replace(",", " ")
    return new_amount


def cli_main():
    cli(obj={})


if __name__ == "__main__":
    cli_main()
