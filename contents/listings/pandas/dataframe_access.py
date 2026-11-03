import pandas as pd

df = pd.DataFrame({"Price": [1.0, 1.4], "Quantity": [5, 10]}, index=["a", "b"])

# Accessing Columns (returns Series or DataFrame)
quantities = df["Quantity"]
two_columns = df[["Price", "Quantity"]]

# Accessing Rows (returns Series)
row_pos = df.iloc[0]
row_label = df.loc["a"]

# Accessing specific blocks
block = df.loc["a":"b", "Price":"Quantity"]

# Masking (filtering rows)
mask = df["Quantity"] < 10
selected_rows = df[mask] # Shorthand for df.loc[mask]