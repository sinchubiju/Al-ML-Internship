import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

plt.plot(x, y)

plt.title("Student Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.show()

import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

plt.plot(x, y, linestyle="--", marker="o", label="Marks")

plt.title("Styled Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.legend()
plt.grid()

plt.show()