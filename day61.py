text = "HELLO, I WANT TO BOOK A TICKET."
print(text.lower())

text = "I love learning Artificial Intelligence."
tokens = text.split()
print(tokens)

sentence = input("Enter a sentence: ")

tokens = sentence.split()

print("Tokens:")

for token in tokens:
    print(token)