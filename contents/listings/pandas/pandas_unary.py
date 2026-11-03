import pandas as pd
import numpy as np

s = pd.Series([-1.0, 2.0, -3.0], index=["a", "b", "c"])

# Arithmetic with a scalar
shifted = s / 4 + 1

# NumPy universal functions work directly on pandas objects
absolute = np.abs(s)