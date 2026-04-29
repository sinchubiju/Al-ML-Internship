
import datetime
import matplotlib.pyplot as plt

# Current date & time
now = datetime.datetime.now()
print(now)

# Format date
print(now.strftime("%Y-%m-%d"))

# Extract year and month
print(now.year)
print(now.month)

# Visualization
x = [1, 2, 3]
y = [10, 20, 30]

plt.plot(x, y)
plt.show()

import matplotlib.pyplot as plt

# Data
x = [1, 2, 3]
y = [10, 20, 30]

# Line graph
plt.plot(x, y)
plt.title("Line Graph")
plt.show()

# Bar chart
plt.bar(x, y)
plt.title("Bar Chart")
plt.show()

# Student marks
students = ["A", "B", "C"]
marks = [80, 70, 90]

plt.bar(students, marks)
plt.title("Student Marks")
plt.show()