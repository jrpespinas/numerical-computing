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
