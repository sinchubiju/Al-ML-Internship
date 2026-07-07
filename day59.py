faq = {
    "fees": "Course fee is ₹15,000.",
    "duration": "Course duration is 3 months.",
    "location": "Our college is located in Kochi.",
    "contact": "Call us at 9876543210.",
    "admission": "Admissions are open now."
}

while True:

    user = input("You: ").lower()

    if user == "bye":
        print("Bot: Thank you!")
        break

    if user in faq:
        print("Bot:", faq[user])

    else:
        print("Bot: Sorry! Please contact our office.")