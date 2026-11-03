import numpy as np

x = np.array([1, 2, 3])          # Shape: (3,)
y = np.array([[11], [12], [13]]) # Shape: (3, 1)

# Rule 1 & 2 apply: x pads to (1,3), stretches to (3,3). 
# y stretches to (3,3). Result is (3,3).
z = x + y  
shifted = x + 10  # A scalar is broadcasted to every cell