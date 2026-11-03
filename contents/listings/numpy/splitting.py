import numpy as np

x = np.array([7, 7, 9, 9, 8])

# Split at specific indices (before element 2 and before element 4)
parts = np.split(x, [2, 4])  

# Split into equal parts (e.g., 3 equal parts)
# This requires the array size to be perfectly divisible by N.
# (Code example context: assumes a perfectly divisible array)

grid = np.array([[1, 2, 3, 11, 12, 13], 
                 [4, 5, 6, 14, 15, 16]])

# Split horizontally into 2 equal parts
left_right = np.hsplit(grid, 2)

# Split vertically into 2 equal parts
top_bottom = np.vsplit(grid, 2)