import matplotlib.pyplot as plt
import numpy as np

height_min = [10, 2, 8]
height_max = [8, 6, 5]
labels = ["Sensor 1", "Sensor 2", "Sensor 3"]

x = np.arange(3)  # [0, 1, 2]
width = 0.4

fig, ax = plt.subplots(figsize=(5, 3))

# Shifting bars to the left and right to group them
ax.bar(x - width / 2, height_min, width=width, label="min")
ax.bar(x + width / 2, height_max, width=width, label="max")

# Setting the custom text labels on the x-axis
ax.set_xticks(x, labels)
ax.legend()