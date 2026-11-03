import pandas as pd

df = pd.DataFrame({
    "k": ["a", "b", "a", "b"], 
    "c1": [2, 10, 3, 15], 
    "c2": [4, 20, 5, 30]
})

# 1. Iterate over groups
for key, group_df in df.groupby("k"):
    pass # group_df is a subset DataFrame for that key

# 2. Aggregate everything (returns DataFrame, key becomes index)
means = df.groupby("k").mean()

# 3. Named Aggregation (Best Practice to avoid multi-level column names)
named = df.groupby("k").agg(
    c1_max=("c1", "max"),
    c1_min=("c1", "min"),
    c2_max=("c2", "max")
).reset_index() # Turns the grouping key "k" back into a normal column

# 4. Filter (keeps entire groups based on a condition)
# Keeps only the rows belonging to groups where the mean of 'c1' > 5
kept = df.groupby("k").filter(lambda g: g["c1"].mean() > 5)