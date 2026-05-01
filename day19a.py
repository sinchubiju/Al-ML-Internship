import numpy as np
# Aggregation
arr = np.array([10, 20, 30, 40])

print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Max:", np.max(arr))
print("Min:", np.min(arr))
  

#   Axis Practice
arr = np.array([[1, 2], [3, 4]])

print("Column-wise sum:", np.sum(arr, axis=0))
print("Row-wise sum:", np.sum(arr, axis=1))

# Filtering
arr = np.array([10, 20, 30, 40, 25])

print("Values > 20:", arr[arr > 20])
print("Even numbers:", arr[arr % 2 == 0])