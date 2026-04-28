students = [
    {"name": "A", "marks": 80},
    {"name": "C", "marks": 40},
    {"name": "E", "marks": 90},
    {"name": "F", "marks": 70}
]

# Sort descending
students.sort(key=lambda x: x["marks"], reverse=True)

print("Sorted:", students)

# Top 3 students
print("Top 3:", students[:3])


students = [
    {"name": "A", "marks": 80},
    {"name": "C", "marks": 40},
    {"name": "E", "marks": 95}
]

result = {"pass": [], "fail": []}

for s in students:
    if s["marks"] >= 50:
        result["pass"].append(s)
    else:
        result["fail"].append(s)

# Count
pass_count = len(result["pass"])
fail_count = len(result["fail"])

print(result)
print("Pass:", pass_count)
print("Fail:", fail_count)


students = [
    {"name": "A", "marks": 80},
    {"name": "C", "marks": 40},
    {"name": "E", "marks": 95}
]

marks = [s["marks"] for s in students]

average = sum(marks) / len(marks)
highest = max(marks)
lowest = min(marks)

print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)