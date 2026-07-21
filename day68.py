from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

print("Model Loaded Successfully!")

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "Artificial Intelligence",
    "Machine Learning",
    "Deep Learning",
    "Python Programming"
]

embeddings = model.encode(sentences)

print(embeddings)