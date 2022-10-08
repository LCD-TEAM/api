import click
import uvicorn

@click.group()
def cli():
    pass

@click.command
def start(host="0.0.0.0", port=8000):
    uvicorn.run("api_methods:app", host=host, port=port, log_level="debug")

cli.add_command(start)

if __name__ == '__main__':
    cli()