from langchain_community.document_loaders import PyPDFLoader

print("Loading PDF...")

loader = PyPDFLoader(r"C:\Users\dell\Downloads\📘 Day 67-RAG.pdf")
documents = loader.load()

print("PDF loaded successfully!")
print("Total pages:", len(documents))
print(documents[0].page_content[:300])

