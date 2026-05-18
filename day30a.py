import matplotlib.pyplot as plt

students = ["A", "B", "C"]
marks = [80, 90, 75]

plt.bar(students, marks)

plt.title("Student Marks Comparison")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()

import matplotlib.pyplot as plt

data = [40, 30, 20, 10]
labels = ["AI", "Web", "Cloud", "Cyber"]

plt.pie(data, labels=labels)

plt.title("Course Popularity")

plt.show()


import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 15, 20, 25]

plt.scatter(x, y)

plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.show()