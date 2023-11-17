import click
import numpy as np
from numpy import pi
import pandas as pd
import sys

args = sys.argv
if(len(args) < 2):
    func = "sin"
    num = 9

else: 
    func = args[1]
    num = args[2]

@click.group()
def function(function_name, number):

    if function_name == "sin":
        sin(number)
    if function_name == "tan":
        tan(number)

@function.command()
@click.argument("number")
def sin(number):
    """List sin up to a given number.

    Args:
        number (int): number of steps to 2*pi

    Returns:
        list: containing the x and sin
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)
    return

@function.command()
@click.argument("number")
def tan(number):
    """List tan up to a given number.

    Args:
        number (int): number of steps to 2*pi

    Returns:
        list: containing x and tan
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)
    return
    
if __name__ == "__main__":
    function()

