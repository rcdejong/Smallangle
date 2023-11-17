import click
import numpy as np
from numpy import pi
import pandas as pd

#Nodig om sin() en tan() te groeperen
@click.group()
def gonio_functions():
    pass

@gonio_functions.command() #Zorgt ervoor dat je de functie via de command line kan oproepen
@click.option(
    "-n",
    "--number",
    default=9,
    ) #Opties voor de argumenten die je (wel of niet) doorgeeft
def sin(number):
    """List sine up to a given number.

    Args:
        number (int): number of steps to 2*pi

    Returns:
        list: containing the x and sine
    """
    x = np.linspace(0, 2 * pi, int(number))
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)

@gonio_functions.command()
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

@gonio_functions.command()
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
    gonio_functions() #De dummy functie wordt hier opgeroepen omdat we sin() of tan() via de command line oproepen

