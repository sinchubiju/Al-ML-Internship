import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# Step slicing
print(arr[::2])

arr2 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# Slice rows and columns
print(arr2[:, 1:3])

import numpy as np

arr = np.array([10, 20, 30, 40])

# Values > 25
print(arr[arr > 25])

# Between range
print(arr[(arr > 10) & (arr < 40)])

# Replace values
arr[arr > 25] = 0
print(arr)