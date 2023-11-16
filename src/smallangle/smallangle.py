import click
import numpy as np
from numpy import pi
import pandas as pd


@click.command()
@click.argument("function_name")
@click.option(
    "-n",
    "--number",   
    default=9,
    help="Nr of steps beyween 0 and 2*pi to calculate the function",
    show_default=True
)

def function(function_name, number):

    if function_name == "sin":
        sin(number)
    if function_name == "tan":
        tan(number)


def sin(number):
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)
    return


def tan(number):
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)
    return
    

if __name__ == "__main__":
    function()
