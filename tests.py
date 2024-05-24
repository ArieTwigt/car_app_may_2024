from utils.calculation_functions import calc_circle
import pytest

def test_value_calc_circle():
    assert calc_circle(10) == 78.53981633974483
    assert calc_circle(20) == 314.1592653589793


def test_negative_value_calc_circle():
    with pytest.raises(ValueError):
        calc_circle(-10)
        calc_circle(0)