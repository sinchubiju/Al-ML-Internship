students = [
    {"name": "A", "marks": 80},
    {"name": "B", "marks": None},
    {"name": "C", "marks": 40},
    {"name": "D", "marks": -10}
]
# Remove None and negative values
cleaned = [s for s in students if s["marks"] is not None and s["marks"] >= 0]
print(cleaned)


students = [
    {"name": "A", "marks": 80},
    {"name": "C", "marks": 40}
]
# Add pass/fail
for s in students:
    s["status"] = "Pass" if s["marks"] >= 50 else "Fail"

# Convert to percentage (assuming out of 100)
for s in students:
    s["percentage"] = s["marks"]

# New calculated field (bonus: grade)
for s in students:
    s["grade"] = "A" if s["marks"] >= 75 else "B"

print(students)