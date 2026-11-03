import numpy as np

x = np.array([[1, 2, 3], [4, 5, 6]])
y = np.array([[11, 12, 13], [14, 15, 16]])

# Vertical stacking (axis=0)
stacked = np.concatenate((x, y))     
vertical = np.vstack((x, y))         # Equivalent to concatenate with axis=0

# Horizontal stacking (axis=1)
side_by_side = np.concatenate((x, y), axis=1) 
horizontal = np.hstack((x, y))       # Equivalent to concatenate with axis=1

# Stacking 1-D arrays into a 2D matrix (creates a new axis)
v1 = np.array([1, 2, 3])
v2 = np.array([11, 12, 13])
rows = np.vstack((v1, v2))           # Resulting shape: (2, 3)