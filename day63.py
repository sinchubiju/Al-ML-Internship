training_data = {
    "hello": "Greeting",
    "hi": "Greeting",
    "bye": "Goodbye",
    "track order": "Order Tracking",
    "refund": "Refund",
    "cancel": "Order Cancellation"
}

user = input("You: ").lower()

for text, intent in training_data.items():
    if text in user:
        print("Predicted Intent:", intent)
        break
else:
    print("Intent not recognized.")