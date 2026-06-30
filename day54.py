from sklearn.feature_extraction.text import CountVectorizer

documents = [
    "I love AI",
    "I love Python"
]

vectorizer = CountVectorizer()

X = vectorizer.fit_transform(documents)

print("Vocabulary:")
print(vectorizer.get_feature_names_out())

print("\nBoW Matrix:")
print(X.toarray())


sentences = [
    "I love AI",
    "AI is amazing",
    "Python is powerful",
    "Machine learning is fun",
    "I love Python"
]

vectorizer = CountVectorizer()

X = vectorizer.fit_transform(sentences)

print("Vocabulary:")
print(vectorizer.get_feature_names_out())

print("\nBoW Matrix:")
print(X.toarray())