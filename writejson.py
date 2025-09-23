import json
data = {"cluster":"Production","status":"healthy","restart":"not running"}

with open("data.json","w") as file:
    json.dump(data,file)

print("completed")