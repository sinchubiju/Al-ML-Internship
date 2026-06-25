text = "I love Machine Learning"
tokens = text.split()
print(tokens)

text = "HELLO WORLD"
print(text.lower())

import string

text = "Python!!! is Awesome???"
clean_text = text.translate(
    str.maketrans('', '', string.punctuation)
)
print(clean_text)

import re

text = "AI 2025 is AMAZING!!!"
text = text.lower()
text = re.sub(r'[^a-zA-Z\s]', '', text)
print(text)