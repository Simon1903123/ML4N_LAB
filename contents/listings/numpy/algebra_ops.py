import numpy as np

m = np.array([[1, 1], [2, 2]])
v = np.array([2, 3])

# Matrix-vector multiplication
matrix_vector = np.dot(m, v)

# Matrix-matrix multiplication using dot or the @ operator
matrix_matrix = np.dot(m, np.array([[2, 2], [1, 1]]))
with_operator = m @ np.array([[2, 2], [1, 1]])