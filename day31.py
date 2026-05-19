import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y1 = [10, 20, 30, 40]
y2 = [40, 30, 20, 10]

plt.plot(x, y1, label="Sales")
plt.plot(x, y2, label="Profit")

plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Multiple Line Graph")

plt.legend()
plt.show()


import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

plt.figure(figsize=(8, 5))

plt.plot(x, y, marker='o', linestyle='--')

plt.title("Customized Graph")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.grid()

plt.show()


import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y1 = [10, 20, 30, 40]
y2 = [40, 30, 20, 10]

plt.subplot(1, 2, 1)
plt.plot(x, y1)
plt.title("Graph 1")

plt.subplot(1, 2, 2)
plt.plot(x, y2)
plt.title("Graph 2")

plt.show()

import matplotlib.pyplot as plt
import random

data = [random.randint(1, 50) for i in range(100)]

plt.hist(data)

plt.title("Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")

plt.show()