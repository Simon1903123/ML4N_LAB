import numpy as np

x = np.array([0.5, 1.0, 3.0, 5.0, 7.0])

# Masking creates a boolean array
mask = x > 4
selected = x[mask]  # Returns a 1-D copy of elements where mask is True

# Combining conditions using bitwise operators (parentheses are mandatory)
between = ~((x < 1) | (x > 5))  # Elements between 1 and 5 (included)
same = (x >= 1) & (x <= 5)      # Same mask, written differently

# Writing through a mask directly modifies the original array
x[x > 4] = 0