import pandas as pd

data = {
    "Hours": [1, 2, 3, 5, 6, 7],
    "Result": [0, 0, 0, 1, 1, 1]
}

df = pd.DataFrame(data)
print(df)


data = {
    "Fever": [98, 99, 101, 102, 103],
    "Disease": [0, 0, 1, 1, 1]
}

df = pd.DataFrame(data)
print(df)


import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

data = {
    "Hours": [1, 2, 3, 5, 6, 7],
    "Result": [0, 0, 0, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[["Hours"]]
y = df["Result"]

model = KNeighborsClassifier(n_neighbors=3)

model.fit(X, y)

prediction = model.predict(
    pd.DataFrame([[4]], columns=["Hours"])
)

print("Prediction:", prediction)


from sklearn.neighbors import KNeighborsClassifier
import pandas as pd

data = {
    "Hours": [1, 2, 3, 5, 6, 7],
    "Result": [0, 0, 0, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[["Hours"]]
y = df["Result"]

for k in [1, 3, 5]:
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X, y)

    pred = model.predict(
        pd.DataFrame([[4]], columns=["Hours"])
    )

    print("K =", k, "Prediction =", pred)

    prediction = model.predict(
    pd.DataFrame([[4]], columns=["Hours"])
)

print(prediction)


import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

data = {
    "Temperature": [98, 99, 101, 102, 103],
    "Disease": [0, 0, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[["Temperature"]]
y = df["Disease"]

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

prediction = model.predict(
    pd.DataFrame([[100]], columns=["Temperature"])
)

print(prediction)

import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

data = {
    "Purchase": [100, 200, 300, 500, 700],
    "Category": [0, 0, 0, 1, 1]
}

df = pd.DataFrame(data)

X = df[["Purchase"]]
y = df["Category"]

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

prediction = model.predict(
    pd.DataFrame([[400]], columns=["Purchase"])
)

print("Customer Category:", prediction)