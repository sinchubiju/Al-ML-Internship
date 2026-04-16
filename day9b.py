
students = [
    {"name": "John", "marks": 80},
    {"name": "Sara", "marks": 90},
    {"name": "Alex", "marks": 70}
]
def get_average(students):
    return sum(s["marks"] for s in students) / len(students)

def get_topper(students):
    return max(students, key=lambda x: x["marks"])

def filter_students(students):
    return [s for s in students if s["marks"] > 75]

print("Average:", get_average(students))
print("Topper:", get_topper(students))
print("Filtered:", filter_students(students))