import pandas as pd

data = {
    "Hours": [1, 2, 3, 5, 6, 7],
    "Result": [0, 0, 0, 1, 1, 1]
}

df = pd.DataFrame(data)
print(df)


data = {
    "Fever": [1, 1, 0, 0, 1],
    "Disease": [1, 1, 0, 0, 1]
}

df = pd.DataFrame(data)
print(df)


data = {
    "Income": [20, 25, 30, 50, 60],
    "Loan": [0, 0, 1, 1, 1]
}

df = pd.DataFrame(data)
print(df)
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

data = {
    "Hours": [1, 2, 3, 5, 6, 7],
    "Result": [0, 0, 0, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[["Hours"]]
y = df["Result"]

model = RandomForestClassifier()

model.fit(X, y)

prediction = model.predict([[5]])

print("Prediction:", prediction)
prediction = model.predict([[4]])
print(prediction)

import pandas as pd
from sklearn.ensemble import RandomForestClassifier

data = {
    "Fever": [1, 1, 0, 0, 1],
    "Disease": [1, 1, 0, 0, 1]
}

df = pd.DataFrame(data)

X = df[["Fever"]]
y = df["Disease"]

model = RandomForestClassifier()
model.fit(X, y)

prediction = model.predict([[1]])

print("Disease Status:", prediction)
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

data = {
    "Income": [20, 25, 30, 50, 60],
    "Loan": [0, 0, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[["Income"]]
y = df["Loan"]

model = RandomForestClassifier()
model.fit(X, y)

prediction = model.predict([[40]])

print("Loan Approval:", prediction)
model = RandomForestClassifier(n_estimators=10)
model.fit(X, y)
print(model.predict([[5]]))
model = RandomForestClassifier(n_estimators=50)
model.fit(X, y)
print(model.predict([[5]]))
model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)
print(model.predict([[5]]))