import pandas as pd

# Create Series
data = pd.Series([10, 20, 30, 40])
print(data)

# Series with custom index
marks = pd.Series([85, 90, 78], index=["Math", "Science", "English"])
print(marks)

# Access Series values
print(marks["Math"])




# Create DataFrame
data = {
    "Name": ["Rahul", "Anu", "Arjun"],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)

# Print DataFrame
print(df)

# Add one more column
df["Grade"] = ["A", "A+", "B"]

print(df)