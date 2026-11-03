import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(5, 3))

# --- Line Plot ---
x = np.linspace(0, 5, 20)
y = np.exp(x)

# Customizing line style, color, and marker
ax.plot(x, y, c="blue", linestyle="none", marker="*", label="Points only")
ax.plot(x, 2*y, c="green", linestyle="--", label="Dashed curve")
ax.legend(loc="upper left")

# --- Scatter Plot ---
fig2, ax2 = plt.subplots(figsize=(5, 3))
x_scat, y_scat = np.random.rand(50), np.random.rand(50)

# Colors and sizes defined per point
colors = x_scat + y_scat
area = 100 * (x_scat + y_scat)

points = ax2.scatter(x_scat, y_scat, c=colors, s=area, cmap="viridis")
fig2.colorbar(points, ax=ax2)  # Adds a legend for the colormap