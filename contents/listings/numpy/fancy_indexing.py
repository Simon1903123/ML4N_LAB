import numpy as np

x = np.array([[0.0, 1.0, 2.0], 
              [3.0, 4.0, 5.0], 
              [6.0, 7.0, 8.0]])

# Single list: indexes entire rows
rows = x[[1, 2]]  

# Two lists: read as pairs of coordinates (1,0) and (2,2)
coordinates = x[[1, 2], [0, 2]]  # Returns array([3., 8.])

# Combining fancy indexing with slicing to get blocks (e.g., rows 1,2 and cols 0,2)
block = x[[1, 2], :][:, [0, 2]]