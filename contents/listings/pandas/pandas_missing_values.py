import pandas as pd
import numpy as np

# --- Missing values in a Series ---
# Python's None is automatically converted to np.nan
s1 = pd.Series([4, None, 5, np.nan])

missing_mask = s1.isna()      # Boolean mask: True where NaN
dropped_s = s1.dropna()       # Removes all NaN values
zeros_s = s1.fillna(0)        # Replaces NaN with 0
forward_s = s1.ffill()        # Replaces NaN with the previous valid value

# --- Missing values in a DataFrame ---
df = pd.DataFrame({
    "Total": [1, 3, 5], 
    "Quantity": [2, np.nan, 6]
}, index=["a", "b", "c"])

# Drops any row containing at least one NaN (drops row "b")
rows_dropped = df.dropna()

# Drops any column containing at least one NaN (drops column "Quantity")
columns_dropped = df.dropna(axis="columns")

# Aggregations automatically ignore NaN values
# The mean of Quantity is (2+6)/2 = 4.0
quantity_mean = df["Quantity"].mean()