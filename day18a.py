
import numpy as np
arr = np.array([10, 20, 30, 40])
print("First Element:", arr[0])
print("Slice:", arr[1:3])

arr2 = np.array([[1, 2], [3, 4]])
print("2D Element:", arr2[0, 1])


arr = np.array([1, 2, 3, 4, 5, 6])

# 1D → 2D
reshaped = arr.reshape(2, 3)
print("Reshaped to 2D:\n", reshaped)

# 2D → 1D
flatten = reshaped.reshape(-1)
print("Flattened to 1D:", flatten)
