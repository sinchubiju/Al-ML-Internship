students = [
    {"name": "John", "marks": 80},
    {"name": "Sara", "marks": 90},
    {"name": "Alex", "marks": 70}
]

# Second highest
sorted_students = sorted(students, key=lambda x: x["marks"], reverse=True)
print("Second Topper:", sorted_students[1])

# Pass/Fail count (pass >= 75)
passed = len([s for s in students if s["marks"] >= 75])
failed = len(students) - passed
print("Passed:", passed)
print("Failed:", failed)

# Convert to dictionary
student_dict = {s["name"]: s["marks"] for s in students}
print("Dictionary:", student_dict)