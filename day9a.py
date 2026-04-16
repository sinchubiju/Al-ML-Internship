students = [
    {"name": "John", "marks": 80},
    {"name": "Sara", "marks": 90},
    {"name": "Alex", "marks": 70}
]

# Filter marks > 75
high_marks = [s for s in students if s["marks"] > 75]
print("Marks > 75:", high_marks)

# Count students
print("Total Students:", len(students))

# Lowest marks
low = min(students, key=lambda x: x["marks"])
print("Lowest:", low)

# Sort students
sorted_students = sorted(students, key=lambda x: x["marks"])
print("Sorted:", sorted_students)