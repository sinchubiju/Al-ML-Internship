import pandas as pd

data = {
    "Name": ["Rahul", "Anu", "Arjun"],
    "Marks": [85, 90, 78],
    "Grade": ["A", "A+", "B"]
}

df = pd.DataFrame(data)

# Access single column
print(df["Name"])

# Access multiple columns
print(df[["Name", "Marks"]])

# Print specific rows
print(df.loc[0])




data = {
    "Name": ["Rahul", "Anu", "Arjun"],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)

# head()
print(df.head())

# tail()
print(df.tail())

# info()
print(df.info())