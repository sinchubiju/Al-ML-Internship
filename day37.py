from sklearn.linear_model import LinearRegression
import pandas as pd

data = {
    "Hours": [1, 2, 3, 4, 5],
    "Marks": [20, 40, 60, 80, 100]
}

df = pd.DataFrame(data)

X = df[["Hours"]]
y = df["Marks"]

model = LinearRegression()

model.fit(X, y)

prediction = model.predict([[6]])

print(prediction)


data = {
    "Experience": [1, 2, 3, 4, 5],
    "Salary": [20000, 30000, 40000, 50000, 60000]
}

df = pd.DataFrame(data)

X = df[["Experience"]]
y = df["Salary"]

model = LinearRegression()

model.fit(X, y)

prediction = model.predict([[6]])

print(prediction)


data = {
    "Ads": [1, 2, 3, 4, 5],
    "Sales": [100, 200, 300, 400, 500]
}

df = pd.DataFrame(data)

X = df[["Ads"]]
y = df["Sales"]

model = LinearRegression()

model.fit(X, y)

prediction = model.predict([[6]])

print(prediction)