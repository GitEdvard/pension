import click
from pension_calc.config import Config

@click.group()
@click.option('--whatif/--not-whatif', default=False)
@click.pass_context
def cli(ctx, whatif):
    ctx.obj['whatif'] = whatif


@cli.command("calculate")
@click.pass_context
def create_cand(ctx):
    config_opener = Config()
    config = config_opener.open_config()
    name = config["name"]
    print(f"name: {name}")


def cli_main():
    cli(obj={})


if __name__ == "__main__":
    cli_main()
