import pandas as pd

df1 = pd.DataFrame({"Total": [1, 3], "Quantity": [2, 4]}, index=["a", "b"])
df2 = pd.DataFrame({"Total": [5, 7], "Quantity": [6, 8], "Liters": [1.0, 2.0]}, index=["c", "d"])

# Concatenation (Stacks vertically by default)
vertical = pd.concat((df1, df2))

# Throws away old index and renumbers sequentially (0, 1, 2, 3...)
renumbered = pd.concat((df1, df2), ignore_index=True)

# Merge (Database-style Join)
dfA = pd.DataFrame({"k1": [0, 1], "c2": ["a", "b"]}, index=["i1", "i2"])
dfB = pd.DataFrame({"k1": [1, 0], "c3": ["b1", "a1"]}, index=["i1", "i2"])

# Joins automatically on the common column "k1"
on_columns = pd.merge(dfA, dfB)

# Joins safely enforcing a one-to-one relationship constraint
safe_merge = pd.merge(dfA, dfB, validate="1:1")