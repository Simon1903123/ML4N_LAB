import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(5, 3))

# Plotting two lines on the same Axes
ax.plot([0, 1, 2], [2, 4, 6])
ax.plot([0, 1, 2], [3, 6, 9])

# Setting attributes explicitly
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_xlim([0, 2])
ax.set_xticks([0, 1, 2])

# Adding a grid
ax.grid()

plt.show()