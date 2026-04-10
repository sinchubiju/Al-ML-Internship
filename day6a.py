text = "python"
print("Reverse:", text[::-1])

text = "madam"
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


    text = "hello"
count = {}
for ch in text:
    count[ch] = count.get(ch, 0) + 1
print(count)



text = "python"
vowels = "aeiou"
v = 0
c = 0

for ch in text:
    if ch in vowels:
        v += 1
    else:
        c += 1

print("Vowels:", v)
print("Consonants:", c)