import click


@click.command()
@click.option("--name", prompt="Enter your name: ", help="your name")
def main(name):
    click.echo(f"Hello, {name}, from todolist!")


if __name__ == "__main__":
    main()
