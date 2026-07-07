while True:
    print("\n===== College Enquiry Chatbot =====")
    print("1. Course Fee")
    print("2. Duration")
    print("3. Eligibility")
    print("4. Location")
    print("5. Contact")
    print("6. Hostel Information")
    print("7. Placement Information")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Course Fee: ₹15,000")

    elif choice == "2":
        print("Duration: 3 Months")

    elif choice == "3":
        print("Eligibility: Plus Two Pass")

    elif choice == "4":
        print("Location: Kochi")

    elif choice == "5":
        print("Contact: 9876543210")
    elif choice == "6":
        print("Hostel Available for Boys and Girls")

    elif choice == "7":
        print("Placement Assistance Available")
    

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")

        responses = {
    "1": "Course Fee: ₹15,000",
    "2": "Duration: 3 Months",
    "3": "Eligibility: Plus Two Pass",
    "4": "Location: Kochi",
    "5": "Contact: 9876543210",
    "6": "Hostel Available",
    "7": "Placement Assistance Available"
}

while True:

    print("\n===== College Chatbot =====")
    print("1. Course Fee")
    print("2. Duration")
    print("3. Eligibility")
    print("4. Location")
    print("5. Contact")
    print("6. Hostel Information")
    print("7. Placement Information")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "8":
        print("Goodbye!")
        break

    print(responses.get(choice, "Invalid Choice"))