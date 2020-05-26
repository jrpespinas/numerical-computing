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

"""Newton's  Method using Python"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys

__version__ = '1.0.0'
__author__ = 'Jan Rodolf Espinas'


def f(x):
    """
    A function that evaluates `x`.

    Parameters
    ----------
    x : int or float
        Any value to be evaluated

    Returns
    -------
    float
        the output of the function

    """
    return -10 + x * (0 + x * (4 + x))


def df(x):
    """
    A derivative of the `f()` that evaluates `x`.

    Parameters
    ----------
    x : int or float
        Any value to be evaluated

    Returns
    -------
    float
        the output of the function

    """
    return x * (8 + (3 * x))


def newtons_method(N, p_0):
    """
    Derived from Taylor Polynomials, Newton's Method
    Approximates `f()` with tangent lines to find the root.

    Parameters
    ----------
    N : int
        Number of iterations
    p_0 : int
        Approximation to `p`

    """
    i = 1
    while i < N:
        p = p_0 - (f(p_0) / df(p_0))
        if abs(p - p_0) < 1e-7:
            print(p)
            break
        i += 1
        p_0 = p


if __name__ == "__main__":
    pass
