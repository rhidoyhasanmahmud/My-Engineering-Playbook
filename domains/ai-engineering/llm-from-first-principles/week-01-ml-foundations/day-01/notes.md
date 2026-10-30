# Day 01 — NumPy, Vectors, Matrices and Dot Products

## Learning objectives

- Explain scalars (0D), vectors (1D), matrices (2D) and higher-rank tensors.
- Distinguish `shape`, `ndim`, `size` and `dtype`.
- Distinguish element-wise multiplication from a dot product.
- Explain the inner-dimension compatibility rule for matrix multiplication.
- Relate matrix operations to token embedding representations.

## Key concepts

A matrix with three rows and four columns has shape `(3, 4)`, `ndim=2` and `size=12`.

For vectors `a` and `b` of length `n`, their dot product is `sum(a[i] * b[i] for i in range(n))`. It returns a scalar. By contrast, element-wise multiplication returns an array of products.

For matrix shapes `(m, n)` and `(n, p)`, the matrix product has shape `(m, p)`. In attention, query-key compatibility is computed using scaled dot products, followed by softmax.

## Exercises

1. Predict shape, ndim and size before executing code.
2. Implement `manual_dot_product` without NumPy reduction operations.
3. Predict matrix multiplication shapes and verify them.
4. Compare Python-loop and NumPy vectorized additions with repeated timing runs.

## Reflection (fill in after completion)

- What did I understand?
- What was confusing?
- What mistakes did I make?
- What evidence proves my solution works?
- How does this connect to LLMs?

## References

- https://numpy.org/doc/stable/user/quickstart.html
- https://numpy.org/doc/stable/reference/generated/numpy.dot.html
