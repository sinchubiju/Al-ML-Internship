import nltk

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')

from nltk.tokenize import word_tokenize

text = "Artificial Intelligence is changing the world."

tokens = word_tokenize(text)

print(tokens)