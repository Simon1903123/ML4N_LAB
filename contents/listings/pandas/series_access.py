import pandas as pd

s1 = pd.Series([2.0, 3.1, 4.5], index=["a", "b", "c"])

# Single elements
by_label = s1.loc["a"]
by_pos = s1.iloc[0]

# Slicing
ordered = pd.Series([10, 20, 30, 40], index=["a", "b", "c", "d"])
slice_labels = ordered.loc["b":"c"] # Includes "c" (stop included)
slice_pos = ordered.iloc[1:3]       # Excludes element at index 3

# Masking and Fancy Indexing
mask = (s1 > 2) & (s1 < 10)
masked = s1.loc[mask]
picked = s1.loc[["a", "c"]]