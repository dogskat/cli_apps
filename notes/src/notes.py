import click
import crud

@click.group()
@click.version_option()
@click.pass_context
def cli(ctx: click.Context) -> None:
    """A simple note-taking app"""
    pass

cli.add_command(crud.create)
cli.add_command(crud.read)
cli.add_command(crud.update)
cli.add_command(crud.delete)
cli.add_command(crud.show)

