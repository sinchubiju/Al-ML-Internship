marks = [80, 90, 70, 60]

# Average
avg = sum(marks) / len(marks)
print("Average:", avg)

# Max and Min
print("Max:", max(marks))
print("Min:", min(marks))
# Count
print("Total Students:", len(marks))



marks = [80, 90, None, -10, 70]
# Remove None values
cleaned = [m for m in marks if m is not None]
# Remove negative values
cleaned = [m for m in cleaned if m >= 0]
print("Cleaned Data:", cleaned)


marks = [80, 40, 90, 30, 76, 88]
# Passed students (>=50)
passed = [m for m in marks if m >= 50]
print("Passed:", passed)

# Marks > 75
high_marks = [m for m in marks if m > 75]
print("Marks > 75:", high_marks)

# Even numbers
even = [m for m in marks if m % 2 == 0]
print("Even Numbers:", even)


marks = [80, 90]
# Convert to percentage
scaled = [m / 100 for m in marks]
print("Percentage:", scaled)

# Multiply values (e.g., bonus +10)
bonus = [m + 10 for m in marks]
print("After Bonus:", bonus)

# Normalize (simple scaling /100)
normalized = [m / 100 for m in marks]
print("Normalized:", normalized)