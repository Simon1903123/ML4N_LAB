import pandas as pd

# Reading a CSV file, skipping the first line (e.g., if it's a useless title)
df = pd.read_csv("mycsv.csv", sep=",", skiprows=1)

# Reading a CSV while explicitly mapping custom strings to NaN
# Without this, columns with "no info" would become text instead of numbers
df_missing = pd.read_csv(
    "mycsv_missing.csv", 
    sep=",", 
    na_values=["no info", "x"]
)

# Writing a DataFrame to CSV
# index=False prevents pandas from writing the row labels as an empty-named column
df.to_csv("saved_data.csv", index=False)

# Saving to other formats (e.g., JSON)
df.to_json("myjson.json")