import click


@click.group()
@click.option('--whatif/--not-whatif', default=False)
@click.pass_context
def cli(ctx, whatif):
    ctx.obj['whatif'] = whatif


@cli.command("calculate")
@click.pass_context
def create_cand(ctx):
    print("hello")


def cli_main():
    cli(obj={})


if __name__ == "__main__":
    cli_main()
