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
import math 

__version__: '1.0.0'
__author__: 'Jan Rodolf Espinas'


sign = lambda x: math.copysign(1,x)

def f(x):
    return (x ** 3) + (4 * (x ** 2)) - 10

def check_root(a,b):
    if f(a)*f(b) < 0:
	return True

def bisection_method(a,b,iterations):
    pass 

def main():
    bisection_method(1,2,15)

if __name__ == '__main__':
    main()
