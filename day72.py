import chromadb

# Create ChromaDB client
client = chromadb.Client()

# Create collection
collection = client.create_collection("internship")

# Sample documents
documents = [
    "AI Internship lasts for 3 months.",
    "Internship fee is ₹5,000.",
    "Placement assistance is available.",
    "Certificates are provided after completion.",
    "Python is used for AI development.",
    "ChromaDB stores document embeddings.",
    "FAISS performs similarity search.",
    "RAG combines retrieval and generation.",
    "Embeddings represent text as vectors.",
    "Top-K retrieval improves answer quality."
]

# IDs
ids = [f"doc{i}" for i in range(1, 11)]

# Store documents
collection.add(
    documents=documents,
    ids=ids
)

print("Documents added successfully!")

# Ask user for a question
query = input("\nEnter your question: ")

# Similarity search
results = collection.query(
    query_texts=[query],
    n_results=3
)

print("\nTop 3 Similar Documents:\n")

for i, doc in enumerate(results["documents"][0], start=1):
    print(f"{i}. {doc}")