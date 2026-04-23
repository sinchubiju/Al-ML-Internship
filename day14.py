import json
data = {"name": "Sara", "marks": 90}
json_data = json.dumps(data)
print(json_data)


import json
json_data = '{"name": "Sara", "marks": 90}'
data = json.loads(json_data)
print(data["name"])

import json
data = {"name": "Alex", "marks": 85}
with open("data.json", "w") as file:
    json.dump(data, file)



import json
with open("data.json", "r") as file:
    data = json.load(file)
print(data)