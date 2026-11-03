import numpy as np

x = np.array([[1, 1], [2, 2]])
y = np.array([[3, 4], [6, 5]])

# Binary element-by-element operations
product = x * y
total = x + y
powers = x ** 2

# Unary element-by-element operations
exponential = np.exp(x)
logarithms = np.log2(np.array([1.0, 2.0, 4.0, 8.0]))