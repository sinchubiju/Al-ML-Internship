sentences = [
    ["i", "love", "ai"],
    ["ai", "is", "amazing"],
    ["i", "love", "python"],
    ["python", "is", "powerful"],
    ["ai", "makes", "life", "easy"]
]

print(sentences)

from gensim.models import Word2Vec

model = Word2Vec(
    sentences,
    vector_size=50,
    window=3,
    min_count=1,
    workers=4
)

print("Word2Vec model trained successfully!")

print(model.wv["ai"])

print(model.wv.most_similar("ai"))