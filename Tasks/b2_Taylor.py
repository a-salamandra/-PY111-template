"""
Taylor series
"""
import math
from itertools import count
from typing import Union

EPSILON = 0.0001

def ex(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """

    exp = 0

    for n in count(0, 1):
        exp_n = pow(x, n)/math.factorial(n)
        exp += exp_n

        if EPSILON > exp_n:
            break
    print(x)
    return exp


def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """
    sin_x = 0

    for n in count(0, 1):
        sin_x_n = (((-1) ** n) / math.factorial((2 * n) + 1)) * (x ** ((2 * n) + 1))
        sin_x += sin_x_n

        if abs(sin_x_n) < EPSILON:
            break
    print(x)
    return sin_x
