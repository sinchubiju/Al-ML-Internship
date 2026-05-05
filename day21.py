import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
reshaped = arr.reshape(2, 3)

print(reshaped)

reshaped_3d = arr.reshape(1, 2, 3)
print(reshaped_3d)

arr2 = np.array([[1, 2], [3, 4]])

flat = arr2.flatten()
print(flat)

print(arr2.flatten())
print(arr2.ravel())

