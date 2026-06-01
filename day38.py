import pandas as pd

data = {
    "Hours": [1, 2, 3, 4, 5, 6],
    "Result": [0, 0, 0, 1, 1, 1]
}

df = pd.DataFrame(data)
print(df)


data = {
    "Fever": [98, 99, 100, 101, 102, 103],
    "Disease": [0, 0, 0, 1, 1, 1]
}

df = pd.DataFrame(data)
print(df)


data = {
    "Messages": [1, 2, 3, 4, 5, 6],
    "Spam": [0, 0, 0, 1, 1, 1]
}

df = pd.DataFrame(data)
print(df)

import pandas as pd
from sklearn.linear_model import LogisticRegression

data = {
    "Hours": [1, 2, 3, 4, 5, 6],
    "Result": [0, 0, 0, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[["Hours"]]
y = df["Result"]

model = LogisticRegression()
model.fit(X, y)

print("Model Trained Successfully")

prediction = model.predict([[5]])
print(prediction)

prediction = model.predict([[2], [4], [7]])
print(prediction)

probability = model.predict_proba([[5]])
print(probability)