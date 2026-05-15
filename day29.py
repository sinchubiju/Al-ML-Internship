import pandas as pd

# Create Dataset
data = {
    "Name": ["Rahul", "Anu", "Arjun", "Meera"],
    "Department": ["AI", "Web", "AI", "Web"],
    "Salary": [50000, 40000, 60000, 45000]
}

df = pd.DataFrame(data)

# Display Dataset
print("Dataset:\n")
print(df)

# Sorting Data
print("\nSort Salary Ascending:\n")
print(df.sort_values("Salary"))

print("\nSort Salary Descending:\n")
print(df.sort_values("Salary", ascending=False))

# Multiple Column Sorting
print("\nSort by Department and Salary:\n")
print(df.sort_values(["Department", "Salary"]))

# Grouping Data
print("\nGroup by Department:\n")
group = df.groupby("Department")
print(group)

# Aggregation
print("\nAverage Salary by Department:\n")
print(df.groupby("Department")["Salary"].mean())

print("\nTotal Salary by Department:\n")
print(df.groupby("Department")["Salary"].sum())

print("\nEmployee Count by Department:\n")
print(df.groupby("Department")["Name"].count())

# Multiple Aggregation
print("\nMultiple Aggregation:\n")
print(df.groupby("Department")["Salary"].agg(["mean", "max", "min"]))

# Value Counts
print("\nDepartment Value Counts:\n")
print(df["Department"].value_counts())