import click
import json
from pathlib import Path
from datetime import datetime

from config import *


@click.command()
@click.argument("title")
@click.option("--content", prompt=True, help="Content of the note")
@click.option("--tags", help="Comma-separated list of tags")
def create(title: str, content: str, tags: str) -> None:
    """Create a new note."""
    notes_directory = Path(f"{proj_dir}/_notes")
    note_name = f"{title}.txt"
    if (notes_directory / note_name).exists():
        click.echo(f"Note with titel '{title}' already exists at {notes_directory}/{note_name}.")
        exit(1)

    note_data = {
        "content": content,
        "tags": tags.split("," if tags else []),
        "created_at": datetime.now().isoformat()
    }
    with open(notes_directory / note_name, "a+") as file:
        json.dump(note_data, file)
    click.echo(f"Note '{title}' created at {notes_directory}/{note_name}.")

@click.command()
def read():
    pass

@click.command()
def update():
    pass

@click.command()
def delete():
    pass

@click.command()
def show():
    pass

