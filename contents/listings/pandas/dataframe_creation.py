import pandas as pd

# Creating from a dictionary of lists
df = pd.DataFrame({
    "Price": [1.0, 1.4, 5.0],
    "Quantity": [5, 10, 8],
    "Liters": [1.5, 0.3, 1.0]
}, index=["a", "b", "c"])

# Inspecting attributes
columns = df.columns
row_labels = df.index
raw_array = df.to_numpy()
dtypes = df.dtypes