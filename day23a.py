

import numpy as np

x = np.array([[1], [2], [3]])
y = np.array([10, 20, 30])

print("Shape of x:", x.shape)
print("Shape of y:", y.shape)

# Compatible shapes
print("\nCompatible Shapes Addition:")
print(x + y)

# Incompatible shapes
a = np.array([1, 2, 3])
b = np.array([1, 2])

print("\nIncompatible Shapes:")
print(a + b)



import numpy as np

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# Add scalar
print("Add Scalar:")
print(matrix + 100)

# Multiply matrix
print("\nMultiply Matrix:")
print(matrix * 2)

# Normalize matrix values
print("\nNormalized Matrix:")
print(matrix / 6)