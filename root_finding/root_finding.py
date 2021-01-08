"""Root-Finding Algorithms"""

# import numpy as np
import math

def check_root(f: 'function', left: float, right: float) -> bool: 
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
    error_bound: float = 1e-7) -> float:
    
    assert check_root(f, left, right), \
        "ERROR: Root does not exist between {} and {}.".format(left, right)

    while abs(right - left) > error_bound:
        midpoint = (left + right) / 2
        if f(midpoint) * f(left) < 0:
            right = midpoint
        else: 
            left = midpoint

    return midpoint

def main():
    print(bisection_method(math.sin, 2, 4))

if __name__ == "__main__":
    main()