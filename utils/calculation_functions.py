import math
from typing import Union

def calc_circle(diameter: Union[float, int]) -> float:
    """
    
    Calculate the size of a circle
    
    """

    # check if the value is not negative
    if diameter <= 0:
        raise ValueError("The diameter cannot be negative or 0")

    radius = diameter / 2
    
    size = math.pow(radius, 2) * math.pi

    return size
