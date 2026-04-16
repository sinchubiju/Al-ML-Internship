# Read data from file
students = []

with open("students.txt", "r") as file:
    for line in file:
        name, marks = line.strip().split(",")
        students.append({"name": name, "marks": int(marks)})

# Print all students
print("Students List:", students)

# Average marks
total = sum(s["marks"] for s in students)
avg = total / len(students)
print("Average:", avg)

# Topper
top = max(students, key=lambda x: x["marks"])
print("Topper:", top["name"])