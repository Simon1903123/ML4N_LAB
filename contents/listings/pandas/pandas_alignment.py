import pandas as pd

# 1. Series Alignment
s1 = pd.Series([3, 1, 10], index=["b", "a", "c"])
s2 = pd.Series([1, 3, 30], index=["a", "b", "d"])

# Aligns by label: 'a' with 'a', 'b' with 'b'. 'c' and 'd' get NaN.
total_s = s1 + s2 

# 2. DataFrame and Series Broadcasting
df = pd.DataFrame({
    "Total": [1, 3, 5], 
    "Quantity": [2, 4, 6]
}, index=["a", "b", "c"])

s3 = pd.Series({"Total": 1, "Quantity": 2})

# The Series index matches the DataFrame columns. 
# It is added to every row automatically.
res = df + s3