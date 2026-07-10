from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

text = "I want to book a train ticket to Delhi."

tokens = word_tokenize(text)

stop_words = set(stopwords.words("english"))

filtered_words = []

for word in tokens:
    if word.lower() not in stop_words:
        filtered_words.append(word)

print(filtered_words)


from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

words = ["Playing", "Running", "Reading", "Learning"]

for word in words:
    print(word, "->", stemmer.stem(word))

    from nltk.tokenize import word_tokenize

print("===== AI College Chatbot =====")
print("Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "bye":
        print("Bot: Goodbye!")
        break

    tokens = word_tokenize(user)

    if "hello" in tokens or "hi" in tokens:
        print("Bot: Hello! How can I help you?")

    elif "fee" in tokens or "fees" in tokens:
        print("Bot: The course fee is ₹15,000.")

    elif "duration" in tokens:
        print("Bot: Course duration is 3 months.")

    elif "eligibility" in tokens:
        print("Bot: Eligibility is Plus Two or equivalent.")

    elif "contact" in tokens:
        print("Bot: Contact Number: 9876543210")

    elif "location" in tokens or "college" in tokens:
        print("Bot: Our college is located in Kochi, Kerala.")

    else:
        print("Bot: Sorry! I couldn't understand.")