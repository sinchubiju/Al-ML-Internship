import numpy as np
arr3 = np.array([[1, 2], [3, 4]])

print(arr3.T)

a = np.array([1, 2])
b = np.array([3, 4])

print(np.vstack((a, b)))

print(np.hstack((a, b)))

arr4 = np.array([1, 2, 3, 4])

print(np.split(arr4, 2))