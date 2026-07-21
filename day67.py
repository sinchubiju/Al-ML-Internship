from PyPDF2 import PdfReader

reader = PdfReader(r"C:\Users\dell\Downloads\📘 Day 67-RAG.pdf")

text = ""

for page in reader.pages:
    text += page.extract_text()

print(text)