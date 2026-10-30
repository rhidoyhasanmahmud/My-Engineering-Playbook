# Week 01 — Numerical Computing Foundations

**Objective:** Learn how arrays and basic mathematical operations support ML model computations.

| Day | Lesson | Exercise |
| --- | --- | --- |
| 01 | NumPy arrays, shapes, vectors, dot products | Predict shapes; implement dot product with validation |
| 02 | Linear algebra and similarity | Implement cosine similarity and verify results |
| 03 | Derivatives and gradients | Implement gradient descent for a scalar function |
| 04 | Neurons and activation functions | Build a two-layer NumPy forward pass |
| 05 | MSE and linear regression | Train a regression model with manual gradients |
| 06 | PyTorch tensors, autograd, MPS | Compare manual gradients and autograd |
| 07 | Mini-project | Compare NumPy and PyTorch regression implementations |

## Day 01 requirements

- Explain scalar, vector, matrix and tensor; predict `shape`, `ndim` and `size`.
- Implement a dot product without `np.dot`, `np.sum` or `@`.
- Raise `ValueError` for unequal vector lengths.
- Multiply compatible matrices and explain the output shape.
- Benchmark equivalent list and NumPy addition workloads fairly.

[Exercise starter](day-01/exercises.py) · [Day 01 notes](day-01/notes.md)

## Week 01 mini-project

Fit noisy synthetic data following `y = 3x + 2 + noise` with NumPy and PyTorch. Track MSE, plot training loss, test shape validation, and document the random seed, environment, learned parameters and limitations. No results should be claimed before running experiments.
