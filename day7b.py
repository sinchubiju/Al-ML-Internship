numbers = [1, 2, 3, 4, 5]
print("Reversed:", numbers[::-1])

text = input("Enter a sentence: ")
words = text.split()
print("Word count:", len(words))

numbers = [1, 2, 2, 3, 4, 4, 5]
unique = list(set(numbers))
print("Without duplicates:", unique)

numbers = [10, 20, 4, 45, 99]
numbers.sort()
print("Second largest:", numbers[-2])