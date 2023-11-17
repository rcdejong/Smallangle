# Name: smallangle.py
# Author: Roland de Jong
# Date created: 17-11-2023

import click
import numpy as np
from numpy import pi
import pandas as pd

# To define the group for the subcommands sine(), tan() and cosine().
@click.group()
def trigonometric_functions():
    pass

@trigonometric_functions.command() # To be able to call the functions via the command line.
# @click.argument("function sine")
@click.option(
    "-n",
    "--number",
    default=9,
    ) # Options for the arguments .

def sin(number):
    """Print a list of the sine(x) function for x from 0 to 2*pi.

    Args:
        number (int): number of steps in the list from 0 to 2*pi.

    Returns:
        printed list: containing the x and sine(x)
    """
    x = np.linspace(0, 2 * pi, int(number))
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)

@trigonometric_functions.command()
@click.option(
    "-n",
    "--number",
    default=9,
    )
def tan(number):
    """List tangent up to a given number.

    Args:
        number (int): number of steps to 2*pi

    Returns:
        list: containing x and tangent
    """
    x = np.linspace(0, 2 * pi, int(number))
    df = pd.DataFrame({"x": x, "tangent (x)": np.tan(x)})
    print(df)

@trigonometric_functions.command()
@click.option(
    "-n",
    "--number",
    default=9,
    )
def cos(number):
    """List cosine up to a given number.

    Args:
        number (int): number of steps to 2*pi

    Returns:
        list: containing x and cosine
    """
    x = np.linspace(0, 2 * pi, int(number))
    df = pd.DataFrame({"x": x, "cosine (x)": np.cos(x)})
    print(df)
if __name__ == "__main__":
    trigonometric_functions() # Calls the dummy function because sine(), tan() or cosine() are called via the command line.
