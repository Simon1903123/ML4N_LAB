import matplotlib.pyplot as plt

# --- 1D Grid: 1 Row, 2 Columns ---
fig1, ax1 = plt.subplots(1, 2, figsize=(5, 2.5))

# ax1 is a 1-D array of shape (2,)
ax1[0].plot([0, 1, 2], [2, 4, 6])  # First plot
ax1[1].plot([0, 1, 2], [3, 6, 9])  # Second plot

fig1.tight_layout()
plt.show()

# --- 2D Grid: 2 Rows, 2 Columns ---
fig2, ax2 = plt.subplots(2, 2, figsize=(5, 4))

# ax2 is a 2-D array of shape (2, 2)
ax2[0, 0].plot([0, 1, 2], [2, 4, 6])  # Top-left
ax2[1, 1].plot([0, 1, 2], [3, 6, 9])  # Bottom-right

fig2.tight_layout()
plt.show()