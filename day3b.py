text = "Hello World"
print(len(text))

text = "Hello"
print(text[::-1])

text = "madam"

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

    text = "Hello World"
vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count += 1

print("Vowels:", count)