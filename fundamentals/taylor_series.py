# Copyright 2020 Jan Rodolf Espinas
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Intro to Numerical Analysis: Taylor Series"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import math

__version__ = '1.0.0'
__author__ = 'Jan Rodolf Espinas'

class TaylorSeries(object):
    def __init__(self, num_terms: int):
        self.num_terms = num_terms
    
    def compute_taylor_series(self, x: float) -> float:
        raise NotImplementedError
    
    def __call__(self, x: float) -> float:
        return self.compute_taylor_series(x)

class Exponential(TaylorSeries):
    def compute_taylor_series(self, x: float) -> float:
        approximation = sum(
            list(
                map(
                    lambda number: (x ** number) / (math.factorial(number)),
                    list(range(self.num_terms))
                )
            )
        )
        return approximation

class Sine(TaylorSeries):
    def compute_taylor_series(self, x: float) -> float:
        approximation = sum(
            list(
                map(
                    lambda number: ((-1) ** number) * (x ** ((2 * number) + 1)) 
                    / (math.factorial(2 * number + 1)),
                    list(range(self.num_terms))
                )
            )
        )
        return approximation

class Cosine(TaylorSeries):
    def compute_taylor_series(self, x: float) -> float:
        approximation = sum(
            list(
                map(
                    lambda number: ((-1) ** number) * (x ** (2 * number))
                    / (math.factorial(2 * number)),
                    list(range(self.num_terms))
                )
            )
        )
        return approximation

def main():
    pass

if __name__ == '__main__':
    main()
