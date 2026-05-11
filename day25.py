import numpy as np

marks = np.array([
    [85, 78, 90],
    [70, 88, 60],
    [95, 92, 89]
])

# Average marks
print("Average Marks:", np.mean(marks))

# Highest marks
print("Highest Marks:", np.max(marks))

# Lowest marks
print("Lowest Marks:", np.min(marks))

# Topper
total = np.sum(marks, axis=1)
topper = np.argmax(total)

print("Total Marks:", total)
print("Top Student Index:", topper)


import numpy as np

image = np.array([
    [50, 100],
    [150, 200]
])

# Increase brightness
bright = image + 50
print("Brightness Increased:")
print(bright)

# Decrease brightness
dark = image - 30
print("Brightness Decreased:")
print(dark)

# Normalize pixels
normalized = image / np.max(image)
print("Normalized Image:")
print(normalized)


import numpy as np

arr = np.array([10, 25, 55, 70, 15, 90])

# Filter values > 50
filtered = arr[arr > 50]
print("Filtered Values:", filtered)

# Replace low values
arr[arr < 20] = 0
print("Updated Array:", arr)

# Count filtered values
count = np.sum(filtered > 50)
print("Count:", count)