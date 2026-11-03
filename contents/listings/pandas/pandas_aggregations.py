import pandas as pd

df = pd.DataFrame({
    "Total": [1, 3, 5], 
    "Quantity": [2, 4, 6]
}, index=["a", "b", "c"])

# Aggregating a DataFrame returns a Series
mean_series = df.mean()
std_series = df.std()  # Divides by n-1. Use ddof=0 to divide by n.

# Z-score normalization using broadcasting
# (df - mean_series) aligns columns and broadcasts across all rows
df_norm = (df - mean_series) / std_series