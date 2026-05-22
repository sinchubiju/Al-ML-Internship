import pandas as pd

data = {
    "StudyHours": [1, 2, 3, 4, 5],
    "Marks": [40, 50, 60, 70, 80],
    "SleepHours": [8, 7, 6, 5, 4]
}

df = pd.DataFrame(data)

print(df)

print("\nCorrelation Matrix:")
print(df.corr())


import seaborn as sns
import matplotlib.pyplot as plt

sns.heatmap(df.corr(), annot=True)

plt.title("Correlation Heatmap")
plt.show()

sns.pairplot(df)

plt.show()

sns.scatterplot(x="StudyHours", y="Marks", data=df)

plt.title("Study Hours vs Marks")
plt.show()

data = {
    "Experience": [1, 2, 3, 4, 5],
    "Salary": [25000, 30000, 35000, 40000, 45000]
}

df = pd.DataFrame(data)

sns.scatterplot(x="Experience", y="Salary", data=df)

plt.show()

data = {
    "Temperature": [20, 25, 30, 35, 40],
    "Sales": [100, 150, 200, 250, 300]
}

df = pd.DataFrame(data)

sns.scatterplot(x="Temperature", y="Sales", data=df)

plt.show()