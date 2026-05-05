import numpy as np

arr = np.array([10, 20, 30, 40])
# First element
print(arr[0])

# Last element
print(arr[-1])

# Slicing
print(arr[1:3])


import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# Access element
print(arr[0, 1])

# Print row
print(arr[1])

# Print column
print(arr[:, 1])


import numpy as np

arr = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]]
])

# Access layer
print(arr[0])

# Access row inside layer
print(arr[0][1])

# Access single element
print(arr[1, 0, 2])