import numpy as np

ones = np.ones((2, 3))
filled = np.full((2, 1), 1.1)

line = np.linspace(0, 1, 11)   # 11 samples, stop included
steps = np.arange(1, 7, 2)     # stop excluded

np.random.seed(2)  # Ensures reproducibility
uniform = np.random.random((2, 3))
normal = np.random.normal(0, 1, (2, 3))