try:
    a = int(input("Enter number: "))
    result = a / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Invalid input! Please enter a number.")

try:
    num = int(input("Enter number: "))
    print(10 / num)
except ZeroDivisionError:
    print("Division by zero error")
except ValueError:
    print("Invalid input")
else:
    print("No error occurred")
finally:
    print("Execution completed")

try:
    with open("sample.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found!")