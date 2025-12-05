import json

data = {"name":"Aamir","age":21}

# Write JSON
with open("data.json","w") as f:
    json.dump(data,f)

# Read JSON
with open("data.json","r") as f:
    result = json.load(f)
