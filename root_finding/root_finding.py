"""Root-Finding Algorithms"""

import math
import numpy as np


__version__ = "1.0.0"
__author__ = "Jan Rodolf Espinas"


def check_root_exist(f: 'function', left: float, right: float) -> bool:
    """Identify if the root exists between two endpoints
    evaluated by function `f`.

    Args: 
        f (function): The function used for evaluating the endpoints.
        left (float): The left endpoint.
        right (float): The right endpoint.

    Returns:
        bool: Returns `True` if the root exists, returns `False` otherwise.
    """
    return True if f(left) * f(right) < 0 else False


def bisection_method(f: 'function', left: float, right: float,
                     tolerance: float = 1e-7) -> float:
    """Find the root guided by the intermediate value theorem and binary 
    search algorithm.

    Args: 
        f (function): The function used for evaluating the endpoints.
        left (float): The left endpoint.
        right (float): The right endpoint.
        tolerance (:obj:`float`, optional): The value which determines when
            the loop should stop.

    Returns:
        midpoint (float): The approximate root.

    Examples:
        >>> approximate_root = bisection_method(math.sin, 2, 4)
        >>> approximate_root = bisection_method(math.cos, 3, 4, 1e-10)
    """

    assert check_root_exist(f, left, right), \
        "ERROR: Root does not exist between {} and {}.".format(left, right)

    while abs(right - left) > tolerance:
        midpoint = (left + right) / 2
        if f(midpoint) * f(left) < 0:
            right = midpoint
        else:
            left = midpoint

    return midpoint


def newtonian_method():
    raise NotImplementedError


def fixed_point_iteration():
    raise NotImplementedError


def main():
    print(bisection_method(math.sin, 2, 4))


if __name__ == "__main__":
    main()
