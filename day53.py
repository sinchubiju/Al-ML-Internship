
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

words = ["Playing", "Working", "Learning", "Running"]

for word in words:
    print(word, "->", stemmer.stem(word.lower()))

    import nltk
nltk.download('wordnet')

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

words = ["cars", "children", "mice", "dogs"]

for word in words:
    print(word, "->", lemmatizer.lemmatize(word))

  
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

words = ["playing", "studies", "running", "mice"]

print("Word\t\tStemmed\t\tLemmatized")

for word in words:
    print(word, "\t", stemmer.stem(word), "\t\t", lemmatizer.lemmatize(word))

    lemmatizer.lemmatize("playing", pos="v")
lemmatizer.lemmatize("running", pos="v")


words = [
    "playing",
    "worked",
    "running",
    "studies",
    "cars",
    "children",
    "mice",
    "dogs",
    "learning",
    "books"
]

print("{:<12} {:<12} {:<12}".format("Word", "Stemmed", "Lemmatized"))

for word in words:
    print("{:<12} {:<12} {:<12}".format(
        word,
        stemmer.stem(word),
        lemmatizer.lemmatize(word)
    ))