import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    "Hours": [1, 2, 3, 4, 5],
    "Marks": [20, 40, 60, 80, 100]
}

df = pd.DataFrame(data)

X = df[["Hours"]]
y = df["Marks"]

model = LinearRegression()

model.fit(X, y)

print("Model Trained Successfully")

prediction = model.predict([[6]])

print("Predicted Marks:", prediction)


data = {
    "Experience": [1, 2, 3, 4, 5],
    "Salary": [25000, 35000, 45000, 55000, 65000]
}

df = pd.DataFrame(data)

X = df[["Experience"]]
y = df["Salary"]

model = LinearRegression()

model.fit(X, y)

prediction = model.predict([[6]])

print("Predicted Salary:", prediction)



data = {
    "Month": [1, 2, 3, 4, 5],
    "Sales": [1000, 1500, 2000, 2500, 3000]
}

df = pd.DataFrame(data)

X = df[["Month"]]
y = df["Sales"]

model = LinearRegression()

model.fit(X, y)

prediction = model.predict([[6]])

print("Predicted Sales:", prediction)