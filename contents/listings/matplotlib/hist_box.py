import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig, (ax_hist, ax_box) = plt.subplots(1, 2, figsize=(10, 4))

# --- Histogram ---
heights = np.random.normal(170, 10, 500)
bins = np.arange(140, 200, 2.5)  # Defining exact bin edges

ax_hist.hist(heights, bins=bins)
# Annotating text at specific data coordinates, using LaTeX formatting
ax_hist.text(142, 40, r"$\mu = 170$", fontsize=10)
ax_hist.set_title("Height distribution")

# --- Box Plot ---
short = np.random.normal(170, 10, 500)
tall = np.random.normal(190, 10, 500)

ax_box.boxplot([short, tall])
ax_box.set_xticks([1, 2], ["Short", "Tall"])
ax_box.set_title("Box Plot Comparison")

fig.tight_layout()

# --- pandas Plotting & Saving ---
# pandas can draw directly onto existing Matplotlib Axes
df = pd.DataFrame({"A": [1, 2], "B": [3, 4]}, index=["row1", "row2"])
df.plot.bar(ax=ax_box)  # Overlays a bar chart on ax_box (example)

# Save the figure to disk
fig.savefig("my_plots.pdf")
plt.close(fig)  # Closes the figure to free memory