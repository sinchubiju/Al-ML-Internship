with open("data.txt", "w") as file:
    file.write("Name: Sinchu\n")
    file.write("Age: 22\n")
    file.write("Course: Python\n")

print("Data written successfully!")


with open("data.txt", "r") as file:
    content = file.read()
    print(content)

with open("data.txt", "a") as file:
       file.write("City: Kerala\n")

print("Data appended!")

with open("data.txt", "r") as file:
    lines = file.readlines()
    print("Number of lines:", len(lines))

with open("data.txt", "r") as file:
    text = file.read()
    words = text.split()
    print("Number of words:", len(words))