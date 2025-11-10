import os
from pathlib import Path

import click


@click.group()
def cli():
    pass


# Test example of click cli
@cli.command()
@click.option('--name', default='User', help='The name to greet.')
def hello(name):
    """A simple hello command to test the CLI setup."""
    click.echo(f"Hello, {name}!")

@click.command()
def download():
    """Command for downloading raw PDB data to `/data/pdb/raw/`."""
    
    pass


if __name__ == '__main__':
    cli()