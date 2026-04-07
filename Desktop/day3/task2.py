student = {
    "name": "John",
    "age": 20,
    "marks": 85
}
print(student)

student["marks"] = 90
print(student)

student["grade"] = "A"
print(student)

for key, value in student.items():
    print(key, ":", value)