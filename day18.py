import numpy as np

# 1D Array
arr1 = np.array([1, 2, 3, 4])
print("1D Array:", arr1)

# 2D Array
arr2 = np.array([[1, 2], [3, 4]])
print("2D Array:\n", arr2)

# 3D Array
arr3 = np.array([[[1, 2], [3, 4]]])
print("3D Array:\n", arr3)

print("Shape:", arr2.shape)
print("Dimensions:", arr2.ndim)
print("Data Type:", arr2.dtype)

print("Zeros:\n", np.zeros((2, 3)))
print("Ones:\n", np.ones((2, 2)))
print("Identity Matrix:\n", np.eye(3))
print("Range Array:", np.arange(1, 10))