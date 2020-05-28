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

"""Evaluating Polynomials using Horner's Method in Python"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__version__ = '1.0.0'
__author__ = 'Jan Rodolf Espinas'


def evaluate(x, k, c, b):
    '''
    Evaluate `x` from a polynomial using Horner's Method.

    Parameters
    ----------
    x : int or float
            The value of x
    k : int
            degrees or the number of terms
    c : int or float
            coefficients
    b : int or float
            base points

    Returns
    -------
    y : int or float
            The output of the polynomial
    '''
    y = c[0]
    for i in range(1, k):
        y = (y * (x - b[i])) + c[i]
    return y


def f(x):
    return (x ** 3) + (4 * (x ** 2)) - 10


if __name__ == "__main__":
    print(evaluate(3, 4, [1, 4, 0, -10], [0, 0, 0, 0]))
    print(f(3))
