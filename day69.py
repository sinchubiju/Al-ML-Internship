import chromadb

# Create client
client = chromadb.Client()

# Create collection
collection = client.create_collection(name="college_data")

# Add documents
collection.add(
    documents=[
        "AI Internship Fee is ₹5000",
        "Duration is 3 Months",
        "Eligibility is Any Degree",
        "Hostel Facility Available",
        "Placement Assistance Provided"
    ],
    ids=["1", "2", "3", "4", "5"]
)

# Search
results = collection.query(
    query_texts=["How long is the internship?"],
    n_results=1
)

# Print output
print("Search Result:")
print(results)