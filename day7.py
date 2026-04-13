text = input("Enter a string: ")
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")


numbers = [10, 25, 5, 40, 15]
largest = max(numbers)
print("Largest number:", largest)


text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for char in text:
    if char in vowels:
        count += 1
print("Number of vowels:", count)


student = {
    "name": "John",
    "age": 20,
    "course": "Python"
}
for value in student.values():
    print(value)