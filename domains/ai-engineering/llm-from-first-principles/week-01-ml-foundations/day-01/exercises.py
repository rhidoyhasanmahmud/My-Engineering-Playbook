"""Day 01 exercises. Implement TODOs before checking against NumPy."""

import numpy as np


def manual_dot_product(a: np.ndarray, b: np.ndarray) -> float:
    """Return a scalar dot product for equal-length 1D vectors.

    Raises:
        ValueError: If either input is not 1D or lengths differ.
    """
    # TODO: Validate dimensions and equal lengths.
    # TODO: Use a Python loop, without np.dot, np.sum or @.
    raise NotImplementedError("Implement manual_dot_product")


def matrix_product_shape(a_shape: tuple[int, int], b_shape: tuple[int, int]) -> tuple[int, int]:
    """Predict output shape of two compatible 2D matrices.

    Raises:
        ValueError: For incompatible inner dimensions.
    """
    # TODO: Implement shape validation and output shape.
    raise NotImplementedError("Implement matrix_product_shape")


if __name__ == "__main__":
    a = np.array([2, 3, 4])
    b = np.array([5, 6, 7])
    print("Expected NumPy reference:", np.dot(a, b))
    print("Your implementation:", manual_dot_product(a, b))
