class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_pass(self):
        return "Pass" if self.marks >= 50 else "Fail"

students = [
    Student("A", 70),
    Student("B", 90),
    Student("C", 40)
]

# Print all students
for s in students:
    print(s.name, s.marks, s.is_pass())

# Find topper
topper = students[0]
for s in students:
    if s.marks > topper.marks:
        topper = s
print("Topper:", topper.name, topper.marks)



class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def check_balance(self):
        return self.balance

acc = BankAccount(1000)
acc.deposit(500)
acc.withdraw(300)

print("Balance:", acc.check_balance())


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def discount(self, percent):
        return self.price - (self.price * percent / 100)

p1 = Product("Laptop", 50000)
print("Price after discount:", p1.discount(10))