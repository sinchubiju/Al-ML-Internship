import seaborn as sns
import matplotlib.pyplot as plt

data = [10, 20, 30, 40, 100]

sns.boxplot(x=data)

plt.title("Box Plot")
plt.show()



courses = ["AI", "Web", "AI", "Cloud", "AI"]

sns.countplot(x=courses)

plt.title("Course Count Plot")
plt.show()