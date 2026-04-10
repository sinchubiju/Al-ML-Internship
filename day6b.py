students = [
    {"name": "A", "marks": 70},
    {"name": "B", "marks": 90}
]

print(students)

students = [
    {"name": "A", "marks": 70},
    {"name": "B", "marks": 90}
]
top = students[0]

for s in students:
    if s["marks"] > top["marks"]:
        top = s

print("Topper:", top)

students = [
    {"name": "A", "marks": 70},
    {"name": "B", "marks": 90}
]

total = 0
for s in students:
    total += s["marks"]

avg = total / len(students)

print("Average:", avg)

students = [
    {"name": "A", "marks": 70},
    {"name": "B", "marks": 40}
]

passed = [s for s in students if s["marks"] >= 50]

print("Passed:", passed)