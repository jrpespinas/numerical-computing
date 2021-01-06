"""Gaussian Elimination"""

import numpy as np


def gaussian_elimination(matrix: np.ndarray):
    return matrix


def main():
    matrix = np.array([[4, 8, -4, 4],
                       [3, 8, 5, -11],
                       [-2, 1, 12, -17]])

    values = gaussian_elimination(matrix)
    print(values)


if __name__ == "__main__":
    main()
