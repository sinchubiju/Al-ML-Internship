from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Load PDF
loader = PyPDFLoader(r"C:\Users\dell\Downloads\📘 Day 67-RAG.pdf")
documents = loader.load()

# Split into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(documents)

print("PDF loaded successfully!")
print("Total pages:", len(documents))
print("Total chunks:", len(chunks))

from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma

embedding = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

db = Chroma.from_documents(chunks, embedding)

docs = db.similarity_search(
    "What is the internship duration?",
    k=3
)