import click
from mylib.bot import scrape


@click.command()
@click.option("--name", help="Web page we want to scrape")
@click.option("--length", help="length of the output from wikipedia")
def cli(name='Microsoft', length=1):
    result = scrape(name, length)
    click.echo(click.style(f"{result}:", fg="white"))


if __name__ == "__main__":
    cli()
