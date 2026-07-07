while True:

    user = input("You: ").lower()

    if "hello" in user:
        print("Bot: Hello!")

    elif "hi" in user:
        print("Bot: Hi!")

    elif "your name" in user:
        print("Bot: My name is AI Chatbot.")

    elif "bye" in user:
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry! I don't understand.")