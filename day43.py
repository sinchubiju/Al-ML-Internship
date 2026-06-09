import pandas as pd

data = {
    "Hours": [1, 2, 3, 5, 6, 7],
    "Result": [0, 0, 0, 1, 1, 1]
}

df = pd.DataFrame(data)
print(df)


data = {
    "Temperature": [98, 99, 100, 102, 103, 104],
    "Disease": [0, 0, 0, 1, 1, 1]
}

df = pd.DataFrame(data)
print(df)

data = {
    "Message_Length": [20, 25, 30, 100, 120, 150],
    "Spam": [0, 0, 0, 1, 1, 1]
}

df = pd.DataFrame(data)
print(df)

import pandas as pd
from sklearn.svm import SVC

data = {
    "Hours": [1, 2, 3, 5, 6, 7],
    "Result": [0, 0, 0, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[["Hours"]]
y = df["Result"]

model = SVC()
model.fit(X, y)

prediction = model.predict([[5]])

print("Prediction:", prediction)

prediction = model.predict([[4]])
print(prediction)

import pandas as pd
from sklearn.svm import SVC

data = {
    "Temperature": [98, 99, 100, 102, 103, 104],
    "Disease": [0, 0, 0, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[["Temperature"]]
y = df["Disease"]

model = SVC()
model.fit(X, y)

prediction = model.predict([[101]])

print(prediction)

import pandas as pd
from sklearn.svm import SVC

data = {
    "Message_Length": [20, 25, 30, 100, 120, 150],
    "Spam": [0, 0, 0, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[["Message_Length"]]
y = df["Spam"]

model = SVC()
model.fit(X, y)

prediction = model.predict([[110]])

print(prediction)