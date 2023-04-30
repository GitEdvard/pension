import click
from pension_calc.config import open_config

@click.group()
@click.option('--whatif/--not-whatif', default=False)
@click.pass_context
def cli(ctx, whatif):
    ctx.obj['whatif'] = whatif


@cli.command("calculate")
@click.pass_context
def create_cand(ctx):
    config = open_config()
    print(f"savings: {config.savings} kr")


def cli_main():
    cli(obj={})


if __name__ == "__main__":
    cli_main()
