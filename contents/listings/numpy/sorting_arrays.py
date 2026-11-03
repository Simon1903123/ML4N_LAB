import numpy as np

x = np.array([[2, 1, 3], 
              [7, 9, 8]])

# Sorting
by_row = np.sort(x)               # Returns a sorted copy along axis -1
x.sort()                          # Sorts 'x' in place

# Argsort: returns indices that would sort the array
order = np.argsort(x)