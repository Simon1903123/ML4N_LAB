import numpy as np

x = np.array([[1, 2], [3, 4], [5, 6]])  # Shape: (3, 2)
y = np.array([11, 12, 13])              # Shape: (3,), pads to (1, 3)

try:
    # Fails Rule 3: comparing dimensions from the right
    # Dim 1: x has 2, y has 3 -> Mismatch!
    z = x + y  
except ValueError as error:
    print("Broadcasting failed!")


