import pandas as pd

# Read CSV file
df = pd.read_csv("students.csv")
df.columns = df.columns.str.strip()

# Print dataset
print(df)

print(df["Name"])

print(df[["Name", "Marks"]])

print(df.loc[0, "Name"])

print(df.loc[0])

print(df.iloc[1])

print(df[0:2])

print(df[df["Marks"] > 80])

print(df[df["City"] == "Kochi"])

print(df[(df["Marks"] > 80) & (df["City"] == "Kochi")])