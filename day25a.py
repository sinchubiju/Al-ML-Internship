import numpy as np

# 1D to 2D
arr = np.arange(12)
reshaped = arr.reshape(3, 4)

print("1D to 2D:")
print(reshaped)

# 2D to 1D
flattened = reshaped.flatten()

print("2D to 1D:")
print(flattened)

# Create 3D dataset
data3d = np.arange(24).reshape(2, 3, 4)

print("3D Dataset:")
print(data3d)


import numpy as np

# Attendance dataset
attendance = np.random.randint(0, 2, size=(5, 7))
print("Attendance Dataset:")
print(attendance)

# Marks dataset
marks = np.random.randint(35, 100, size=(5, 3))
print("Marks Dataset:")
print(marks)

# Weather dataset
weather = np.random.randint(20, 40, size=(7,))
print("Weather Dataset:")
print(weather)