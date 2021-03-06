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

"""Error Analysis: Intro to Numerical Analysis"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__version__ = '1.0.1'
__author__ = 'Jan Rodolf Espinas'


def absolute_error(true_fx, approximate_fx):
    return abs(true_fx - approximate_fx)


def relative_error(true_fx, approximate_fx):
    return absolute_error(true_fx, approximate_fx)/abs(true_fx)


def main():
    print(relative_error(10, 9))


if __name__ == '__main__':
    main()
