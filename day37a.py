from sklearn.linear_model import LogisticRegression
import pandas as pd

data = {
    "Hours": [1, 2, 3, 4, 5],
    "Result": [0, 0, 0, 1, 1]
}

df = pd.DataFrame(data)

X = df[["Hours"]]
y = df["Result"]

model = LogisticRegression()

model.fit(X, y)

prediction = model.predict([[6]])

print(prediction)


data = {
    "Links": [1, 2, 3, 4, 5],
    "Spam": [0, 0, 0, 1, 1]
}

df = pd.DataFrame(data)

X = df[["Links"]]
y = df["Spam"]

model = LogisticRegression()

model.fit(X, y)

prediction = model.predict([[6]])

print(prediction)



data = {
    "Symptoms": [1, 2, 3, 4, 5],
    "Disease": [0, 0, 0, 1, 1]
}

df = pd.DataFrame(data)

X = df[["Symptoms"]]
y = df["Disease"]

model = LogisticRegression()

model.fit(X, y)

prediction = model.predict([[6]])

print(prediction)