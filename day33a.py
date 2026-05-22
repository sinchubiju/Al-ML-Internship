import pandas as pd

data = {
    "StudyHours": [2, 4, 6, 8],
    "Marks": [50, 60, 75, 90]
}

df = pd.DataFrame(data)

print(df.corr())


data = {
    "Experience": [1, 3, 5, 7],
    "Salary": [20000, 30000, 45000, 60000]
}

df = pd.DataFrame(data)

print(df.corr())



data = {
    "ExerciseHours": [1, 2, 3, 4],
    "Weight": [80, 75, 70, 65]
}

df = pd.DataFrame(data)

print(df.corr())