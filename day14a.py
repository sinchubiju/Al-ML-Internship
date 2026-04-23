import csv
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "marks"])
    writer.writerow(["John", 80])
    writer.writerow(["Sara", 90])

import csv
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


import csv
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # skip header
    for row in reader:
        print(f"Name: {row[0]}, Marks: {row[1]}")


import csv
import json
data_list = []
with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        data_list.append(row)
with open("output.json", "w") as file:
    json.dump(data_list, file)

print(data_list)