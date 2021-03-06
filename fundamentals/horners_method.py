# Copyright 2021 Jan Rodolf Espinas
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

from typing import List

__version__ = '2.0.0'
__author__ = 'Jan Rodolf Espinas'


def horner_method(degree: int, x: float, coefficients: List[float]) -> float:
    """Efficient way to evaluate polynomials.

    Args:
        degree (int): highest exponent of a variable 
            with a non-zero coefficient.
        x (float): the value substituted to the variable.
        coefficients (:obj:`List` of :obj:`float`:): the coefficients
            of the polynomial. 
        
    Returns:
        c (float): the evaluation of the polynomial.
    """
    c = coefficients[0]
    for i in range(1, degree + 1):
        c = coefficients[i] + (c * x)

    return c