import pandas as pd
import numpy as np

# Create Dataset with Missing Values
data = {
    "Name": ["Rahul", "Anu", "Arjun", None],
    "Marks": [85, np.nan, 78, 90],
    "City": ["Kochi", "Trivandrum", None, "Kollam"]
}

df = pd.DataFrame(data)

print("Original Dataset")
print(df)

# Detect Missing Values
print("\nMissing Values Detection")
print(df.isnull())

# Count Missing Values
print("\nCount Missing Values")
print(df.isnull().sum())

# Drop Rows with Missing Values
print("\nDrop Rows with Missing Values")
print(df.dropna())

# Drop Columns with Missing Values
print("\nDrop Columns with Missing Values")
print(df.dropna(axis=1))

# Fill Missing Values with Text
print("\nFill Missing Values with 'Unknown'")
print(df.fillna("Unknown"))

# Fill Numeric Missing Values with Mean
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

print("\nDataset After Filling Mean")
print(df)

# Create Duplicate Row
df2 = pd.concat([df, df.iloc[[0]]], ignore_index=True)

print("\nDataset with Duplicate Row")
print(df2)

# Detect Duplicates
print("\nDuplicate Rows")
print(df2.duplicated())

# Remove Duplicates
print("\nAfter Removing Duplicates")
print(df2.drop_duplicates())

# Rename Column
df.rename(columns={"Marks": "Score"}, inplace=True)

print("\nAfter Renaming Column")
print(df)

# Change Data Type
df["Score"] = df["Score"].astype(int)

print("\nData Types")
print(df.dtypes)