import numpy as np

# --- Single Array ---
x = np.arange(10)
np.save("my_array.npy", x)

loaded_x = np.load("my_array.npy")

# --- Multiple Arrays ---
y = np.arange(3)
np.savez("archive.npz", my_x=x, my_y=y)

archive = np.load("archive.npz")
names = archive.files       # Returns ['my_x', 'my_y']
first_array = archive["my_x"]