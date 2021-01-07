"""Collection of Numerical Algorithms"""

import numpy as np
from typing import List


class NumericalMethods:
    @staticmethod
    def horners_method(degree: int, x: float, coefficients: List[float]):
        c = coefficients[0]
        for i in range(1, degree + 1):
            c = coefficients[i] + (c * x)
        
        return c