import numpy as np

x = np.array([[1, 7], 
              [2, 4]])

# Aggregating the entire array
total = x.sum()
position = x.argmax()  # Returns 1 (position of '7' in flattened array)

# Aggregating along an axis
row_sums = x.sum(axis=-1)        # Sum per row -> array([8, 6])
col_argmax = x.argmax(axis=0)    # Index of largest per column -> array([1, 0])