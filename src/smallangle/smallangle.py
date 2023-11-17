# Name: smallangle.py
# Author: Roland de Jong
# Date created: 17-11-2023

import click
import numpy as np
from numpy import pi
import pandas as pd

# Defines the group for the subcommands sine(), tan() and cosine().
@click.group()
def trigonometric_functions(): 
    """smallangle.py prints a list of trigonometric functions for (not so small...) angles from 0 to 2*pi.
    """
    pass

@trigonometric_functions.command()
@click.option(
    "-n",
    "--number",
    default=9,
    help="Nr of steps beyween 0 and 2*pi to calculate the function",
    show_default=True
    )

def cos(number):
    """Print a list of the cosine function values for angles from 0 to 2*pi. \f

    Args:
        number (int): number of steps in the list from 0 to 2*pi.

    Returns:
        printed list: containing the function arguments (angles) and the function value.
    """
    x = np.linspace(0, 2 * pi, int(number))
    df = pd.DataFrame({"x": x, "cos (x)": np.cos(x)})
    print(df)

@trigonometric_functions.command()
@click.option(
    "-n",
    "--number",
    default=9,
    help="Nr of steps beyween 0 and 2*pi to calculate the function",
    show_default=True
    )

def sin(number):
    """Print a list of the sine function values for angles from 0 to 2*pi. \f

    Args:
        number (int): number of steps in the list from 0 to 2*pi.

    Returns:
        printed list: containing the function arguments (angles) and the function value.
    """
    x = np.linspace(0, 2 * pi, int(number))
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)

@trigonometric_functions.command()
@click.option(
    "-n",
    "--number",
    default=9,
    help="Nr of steps beyween 0 and 2*pi to calculate the function",
    show_default=True
    )

def tan(number):
    """Print a list of the tangent function values for angles from 0 to 2*pi. \f

    Args:
        number (int): number of steps in the list from 0 to 2*pi.

    Returns:
        printed list: containing the function arguments (angles) and the function value.
    """
    x = np.linspace(0, 2 * pi, int(number))
    df = pd.DataFrame({"x": x, "tangent (x)": np.tan(x)})
    print(df)

# Calls the dummy function because sine(), tan() or cosine() are called via the command line.
if __name__ == "__main__":
    trigonometric_functions()
