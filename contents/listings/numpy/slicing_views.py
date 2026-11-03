import numpy as np

x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Slicing returns a VIEW: modifying it changes 'x'
view = x[:, 1:] 
view[:, :] = 0  
# x is now [[1, 0, 0], [4, 0, 0], [7, 0, 0]]

# To protect the original array, use .copy()
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
safe_copy = x[:, 1:].copy()
safe_copy[:, :] = 0  # x remains unchanged