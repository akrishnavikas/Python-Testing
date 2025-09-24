import json
data = {"cluster":"Production","status":"healthy","restart":"not running"}

with open("data.json","w") as file:
    json.dump(data,file)

print("completed")

def read_json():
    with open("data.json","r") as file:
        data = json.load(file)
        print(data)

read_json()