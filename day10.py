class Car:
    name = ""
    price = 0
c1 = Car()
c1.name = "BMW"
c1.price = 5000000
print(c1.name, c1.price)


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

s1 = Student("Sara", 90)
print(s1.name, s1.marks)


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def check_result(self):
        if self.marks >= 50:
            return "Pass"
        else:
            return "Fail"

    def grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 70:
            return "B"
        else:
            return "C"

s1 = Student("Alex", 75)

print(s1.name)
print(s1.check_result())
print(s1.grade())