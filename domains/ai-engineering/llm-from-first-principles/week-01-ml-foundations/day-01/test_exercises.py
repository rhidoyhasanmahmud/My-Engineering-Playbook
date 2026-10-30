"""Tests intentionally expect the learner to complete the TODO implementations."""

import numpy as np
import pytest

from exercises import manual_dot_product, matrix_product_shape


@pytest.mark.parametrize(
    "a,b",
    [
        ([2, 3, 4], [5, 6, 7]),
        ([0, -2, 4], [5, 3, -1]),
        ([], []),
    ],
)
def test_dot_product_matches_numpy(a, b):
    assert manual_dot_product(np.array(a), np.array(b)) == pytest.approx(float(np.dot(a, b)))


def test_dot_product_rejects_mismatched_lengths():
    with pytest.raises(ValueError):
        manual_dot_product(np.array([1, 2]), np.array([1]))


def test_dot_product_rejects_non_vectors():
    with pytest.raises(ValueError):
        manual_dot_product(np.ones((2, 2)), np.ones((2, 2)))


def test_matrix_product_shape():
    assert matrix_product_shape((2, 3), (3, 4)) == (2, 4)


def test_matrix_product_shape_rejects_incompatible_shapes():
    with pytest.raises(ValueError):
        matrix_product_shape((2, 3), (2, 4))
