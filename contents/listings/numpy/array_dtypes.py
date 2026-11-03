import numpy as np

whole = np.array([0, 1, 2]).dtype  # Inferred as int
mixed = np.array([1, 2.5]).dtype   # Upcasted to float64
small = np.array([0.0, 1.0, 2.0], dtype=np.float16).dtype  # Explicitly defined