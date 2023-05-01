import click
from pension_calc.calculator import Calculator
from pension_calc.presenter import Presenter

@click.group()
@click.option('--whatif/--not-whatif', default=False)
@click.pass_context
def cli(ctx, whatif):
    ctx.obj['whatif'] = whatif
    ctx.obj["presenter"] = Presenter()


@cli.command("accomodation")
@click.pass_context
def accomodation(ctx):
    calculator = Calculator()
    a = calculator.accomodation_cost_now()
    ctx.obj["presenter"].accomodation(a)


@cli.command("accomodation_pension")
@click.pass_context
def accomodation_pension(ctx):
    calculator = Calculator()
    a = calculator.accomodation_cost_pension()
    ctx.obj["presenter"].accomodation_pension(a)



@cli.command("growth")
@click.pass_context
def growth(ctx):
    calculator = Calculator()
    g = calculator.return_on_savings()
    ctx.obj["presenter"].growth(g)


@cli.command("payment")
@click.pass_context
def payment(ctx):
    calculator = Calculator()
    p = calculator.pension_payment()
    ctx.obj["presenter"].payment(p)


def cli_main():
    cli(obj={})


if __name__ == "__main__":
    cli_main()
