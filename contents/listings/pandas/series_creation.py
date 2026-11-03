import pandas as pd

# From a list with explicit labels
s2 = pd.Series([2.0, 3.1, 4.5], index=["mon", "tue", "wed"])

# From a dictionary (keys become the index)
s3 = pd.Series({"c": 2.0, "b": 3.1, "a": 4.5})

index = s2.index    # An Index object
values = s2.values  # A NumPy array