import seaborn as sns
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

sns.set_style("darkgrid")
sns.lineplot(x=x, y=y)

plt.title("Line Plot")
plt.show()


students = ["A", "B", "C"]
marks = [85, 90, 78]

sns.barplot(x=students, y=marks)

plt.title("Student Marks Comparison")
plt.show()


x = [1, 2, 3, 4]
y = [5, 10, 15, 20]

sns.scatterplot(x=x, y=y)

plt.title("Scatter Plot")
plt.show()


data = [10, 20, 20, 30, 40, 40, 50]

sns.histplot(data)

plt.title("Histogram")
plt.show()