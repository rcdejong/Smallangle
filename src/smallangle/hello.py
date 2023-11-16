import click
import time

@click.command()
@click.argument("name1")
@click.option(
    "-c",
    "--count",   
    default=1,
    help="Number of times to print greeting.", 
    show_default=True
)
@click.option(
    "-p",
    "--pause",
    default=0,
    help="Seconds pause between greeting prints.",
    show_default=True
)
def hello_there(name1, count, pause):
    for _ in range(count):
        print(f"HelloTjo {name1}!")
        time.sleep(pause)

if __name__ == "__main__":
    hello_there()
