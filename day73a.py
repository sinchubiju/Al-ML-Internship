from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document

# Embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Sample documents
documents = [
    Document(page_content="Artificial Intelligence enables machines to perform tasks that normally require human intelligence."),
    Document(page_content="Machine Learning is a subset of Artificial Intelligence that learns from data."),
    Document(page_content="Deep Learning uses neural networks with multiple layers."),
    Document(page_content="RAG stands for Retrieval-Augmented Generation and combines retrieval with LLMs."),
    Document(page_content="Embeddings convert text into numerical vectors for semantic search."),
    Document(page_content="ChromaDB is a vector database used to store and retrieve embeddings.")
]

# Create vector store
vectorstore = Chroma.from_documents(
    documents=documents,
    embedding=embeddings,
    persist_directory="./chroma_db"
)

# Convert to retriever
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# Five user questions
questions = [
    "What is Artificial Intelligence?",
    "Explain Machine Learning.",
    "What is Deep Learning?",
    "What is RAG?",
    "What are embeddings?"
]

# Retrieve top 3 chunks
for i, question in enumerate(questions, start=1):
    print(f"\nQuestion {i}: {question}")
    results = retriever.invoke(question)

    for j, doc in enumerate(results, start=1):
        print(f"\nTop {j}:")
        print(doc.page_content)