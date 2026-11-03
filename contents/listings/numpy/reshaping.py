import numpy as np

x = np.arange(6)  # [0, 1, 2, 3, 4, 5]

# Reshape into a 2x3 matrix
y = x.reshape((2, 3))

# Create a column vector using the -1 wildcard
column = np.array([1, 2, 3]).reshape(-1, 1)

# This will fail because 6 elements cannot fit into a 4x2 matrix (8 elements)
# invalid_shape = x.reshape((4, 2))