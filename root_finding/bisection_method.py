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
"""Bisection Method using Python"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys

__version__ = '1.0.0'
__author__ = 'Jan Rodolf Espinas'


TOL = 1e-6


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
    return (x ** 3) + (4 * (x ** 2)) - 10


def check_root(a, b):
    """
    Verify if the root exist by checking the signs of `a` and `b`.

    Parameters
    ----------
    a : int
        Left endpoint
    b : int
        Right endpoint

    Return
    ------
    bool:
        Returns True if a root exist

    """
    if f(a) * f(b) < 0:
        return True


def bisection_method(a, b, iterations):
    """
    A root-finding algorithm which uses an iterative method.

    Parameters
    ----------
    a : int or float
        left endpoint
    b : int or float
        right endpoint
    iterations : int
        number of iterations

    """
    if check_root(a, b):
        i = 0
        while i < iterations:
            c = (a + b) / 2
            root = f(c)
            tol = (b - a) / 2
            if root == 0 or tol <= TOL:
                break
            if root * f(a) < 0:
                b = c
            else:
                a = c

            verbosity = f'{i+1}:\ta={a:.6f},\tb={b:.6f},\tc={c:.6f},\troot={root:.6f}'
            if len(sys.argv) > 1:
                print()
            else:
                print(f'{i+1}:\t root = {root:.6f},\ttolerance = {tol:.6f}')

            i += 1
        else:
            print("Root does not exist")


if __name__ == '__main__':
    bisection_method(1, 2, 20)
