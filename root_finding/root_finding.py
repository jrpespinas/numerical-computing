"""Root-Finding Algorithms"""

# import numpy as np

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


def main():
    

if __name__ == "__main__":
    main()