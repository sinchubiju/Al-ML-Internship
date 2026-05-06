import numpy as np

arr = np.array([10, 20, 30, 40])

print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Max:", np.max(arr))
print("Min:", np.min(arr))

print("Median:", np.median(arr))
print("Standard Deviation:", np.std(arr))
print("Variance:", np.var(arr))


arr2 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("Column-wise Sum:", np.sum(arr2, axis=0))
print("Row-wise Sum:", np.sum(arr2, axis=1))
print("Mean (Column-wise):", np.mean(arr2, axis=0))

print("Index of Max:", np.argmax(arr))
print("Index of Min:", np.argmin(arr))

arr3 = np.array([1, 2, 3, 4])

print("Cumulative Sum:", np.cumsum(arr3))