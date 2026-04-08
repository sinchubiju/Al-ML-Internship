with open("data.txt", "r") as file:
    words = file.read().split()
    longest = max(words, key=len)
    print("Longest word:", longest)

with open("data.txt", "r") as file:
    text = file.read().lower()
    vowels = "aeiou"
    count = sum(1 for char in text if char in vowels)
    print("Vowel count:", count)

with open("data.txt", "r") as file:
    lines = file.readlines()

unique_lines = list(set(lines))

with open("data.txt", "w") as file:
    file.writelines(unique_lines)

print("Duplicate lines removed!")