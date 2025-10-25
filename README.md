# functions-from-zero
live training

[![Python application test with Github Actions](https://github.com/Yaribar/functions-from-zero/actions/workflows/main.yml/badge.svg)](https://github.com/Yaribar/functions-from-zero/actions/workflows/main.yml)

import click

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(f"Hello {name}!")

if __name__ == '__main__':
    hello()
