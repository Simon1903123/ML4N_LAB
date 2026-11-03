import pandas as pd

df = pd.DataFrame({"Price": [1.0, 1.4], "Quantity": [5, 10]}, index=["a", "b"])

# Adding a new computed column
df["Total"] = df["Price"] * df["Quantity"]

# Dropping a column (returns a new DataFrame)
df_clean = df.drop(columns=["Total"])

# Modifying data correctly (Single statement)
df.loc["a", "Price"] = 99.0

# INCORRECT modification (modifies a copy in Pandas 3.0+)
prices = df["Price"]
prices.loc["b"] = 100.0  # df["Price"]["b"] remains 1.4