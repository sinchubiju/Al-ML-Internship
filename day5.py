text = "Python"
print(text[::-1])

text = "AI ML Python"
words = text.split()
print(len(words))

text = "madam"
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

    text = "hello ai"
print(text.replace("ai", "ml"))

text = "artificial intelligence"
vowels = "aeiou"
count = 0

for ch in text:
    if ch in vowels:
        count += 1

print(count)