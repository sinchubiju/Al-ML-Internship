from sklearn.feature_extraction.text import TfidfVectorizer

documents = [
    "AI is amazing",
    "AI is powerful",
    "Machine learning is amazing"
]

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(documents)

print(X.toarray())

print(vectorizer.get_feature_names_out())

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

documents = [
    "AI is amazing",
    "AI is powerful",
    "Machine learning is amazing"
]

# Bag of Words
bow = CountVectorizer()
bow_matrix = bow.fit_transform(documents)

print("Bag of Words")
print(bow.get_feature_names_out())
print(bow_matrix.toarray())

# TF-IDF
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(documents)

print("\nTF-IDF")
print(tfidf.get_feature_names_out())
print(tfidf_matrix.toarray())

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

documents = [
    "AI is amazing",
    "AI is powerful",
    "Machine learning is amazing"
]

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(documents)

feature_names = vectorizer.get_feature_names_out()

scores = X.toarray()

df = pd.DataFrame(scores, columns=feature_names)

print(df)