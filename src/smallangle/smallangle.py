import click
import numpy as np
from numpy import pi
import pandas as pd

#Nodig om sin() en tan() te groeperen
@click.group()
def func():
    pass

@func.command() #Zorgt ervoor dat je de functie via de command line kan oproepen
@click.option(
    "-n",
    "--number",
    default=9,
    ) #Opties voor de argumenten die je (wel of niet) doorgeeft
def sin(number):
    """List sin up to a given number.

    Args:
        number (int): number of steps to 2*pi

    Returns:
        list: containing the x and sin
    """
    x = np.linspace(0, 2 * pi, int(number))
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)

@func.command()
@click.option(
    "-n",
    "--number",
    default=9,
    )
def tan(number):
    """List tan up to a given number.

    Args:
        number (int): number of steps to 2*pi

    Returns:
        list: containing x and tan
    """
    x = np.linspace(0, 2 * pi, int(number))
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)

if __name__ == "__main__":
    func() #De dummy functie wordt hier opgeroepen omdat we sin() of tan() via de command line oproepen