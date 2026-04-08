students = [
    {"name": "A", "marks": 70},
    {"name": "B", "marks": 80},
    {"name": "C", "marks": 90},
    {"name": "D", "marks": 60},
    {"name": "E", "marks": 85}
]
for s in students:
    print(s)


total = 0
for s in students:
    total += s["marks"]
avg = total / len(students)
print(avg)


max_marks = 0
for s in students:
    if s["marks"] > max_marks:
        max_marks = s["marks"]
print(max_marks)



for s in students:
    if s["marks"] > 75:
        print(s["name"])