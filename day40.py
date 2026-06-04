import pandas as pd

data = {
    "Hours":[1,2,3,5,6,7],
    "Result":[0,0,0,1,1,1]
}

df = pd.DataFrame(data)
print(df)

import pandas as pd

data = {
    "Income":[15000,20000,25000,40000,50000],
    "Approved":[0,0,1,1,1]
}

df = pd.DataFrame(data)
print(df)

import pandas as pd

data = {
    "Temperature":[98,99,100,101,102],
    "Disease":[0,0,1,1,1]
}

df = pd.DataFrame(data)
print(df)

import pandas as pd
from sklearn.tree import DecisionTreeClassifier

data = {
    "Hours":[1,2,3,5,6,7],
    "Result":[0,0,0,1,1,1]
}

df = pd.DataFrame(data)

X = df[["Hours"]]
y = df["Result"]

model = DecisionTreeClassifier()

model.fit(X,y)

print("Model Trained Successfully")

prediction = model.predict([[5]])
print(prediction)

prediction = model.predict([[2],[5],[8]])
print(prediction)

import pandas as pd
from sklearn.tree import DecisionTreeClassifier

data = {
    "Temperature":[98,99,100,101,102],
    "Disease":[0,0,1,1,1]
}

df = pd.DataFrame(data)

X = df[["Temperature"]]
y = df["Disease"]

model = DecisionTreeClassifier()

model.fit(X,y)

prediction = model.predict([[101]])

print(prediction)

import pandas as pd
from sklearn.tree import DecisionTreeClassifier

data = {
    "Income":[15000,20000,25000,40000,50000],
    "Approved":[0,0,1,1,1]
}

df = pd.DataFrame(data)

X = df[["Income"]]
y = df["Approved"]

model = DecisionTreeClassifier()

model.fit(X,y)

prediction = model.predict([[30000]])

print(prediction)