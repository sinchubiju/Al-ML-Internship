import pandas as pd

data = {
    "Hours":[1,2,3,5,6,7],
    "Result":[0,0,0,1,1,1]
}

df = pd.DataFrame(data)
print(df)

import pandas as pd

data = {
    "Fever":[1,1,0,1,0],
    "Disease":[1,1,0,1,0]
}

df = pd.DataFrame(data)
print(df)

import pandas as pd

data = {
    "Contains_Offer":[1,1,0,0],
    "Spam":[1,1,0,0]
}

df = pd.DataFrame(data)
print(df)

import pandas as pd
from sklearn.naive_bayes import GaussianNB

data = {
    "Hours":[1,2,3,5,6,7],
    "Result":[0,0,0,1,1,1]
}

df = pd.DataFrame(data)

X = df[["Hours"]]
y = df["Result"]

model = GaussianNB()

model.fit(X,y)

prediction = model.predict([[5]])

print("Prediction:", prediction)

prediction = model.predict([[4]])
print(prediction)

import pandas as pd
from sklearn.naive_bayes import GaussianNB

data = {
    "Fever":[1,1,0,1,0],
    "Disease":[1,1,0,1,0]
}

df = pd.DataFrame(data)

X = df[["Fever"]]
y = df["Disease"]

model = GaussianNB()
model.fit(X,y)

prediction = model.predict([[1]])

print(prediction)

import pandas as pd
from sklearn.naive_bayes import GaussianNB

data = {
    "Offer":[1,1,0,0],
    "Spam":[1,1,0,0]
}

df = pd.DataFrame(data)

X = df[["Offer"]]
y = df["Spam"]

model = GaussianNB()
model.fit(X,y)

prediction = model.predict([[1]])

print(prediction)

total_emails = 200
spam_emails = 150

p_spam = spam_emails / total_emails
p_not_spam = (total_emails - spam_emails) / total_emails

print("Probability of Spam:", p_spam)
print("Probability of Not Spam:", p_not_spam)