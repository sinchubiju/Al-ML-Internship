responses = {
    "hello": "Hello!",
    "hi": "Hi!",
    "your name": "I'm AI Bot."
}

while True:

    user = input("You: ").lower()

    if user == "bye":
        print("Bot: Goodbye!")
        break

    print("Bot:", responses.get(user,
    "Sorry, I don't understand your question."))