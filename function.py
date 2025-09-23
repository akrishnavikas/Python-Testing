details = {"hdfs": "running", "yarn": "stopped", "hive": "running"}

def check_service(data):
    for service,status in data.items():
        if status == "running":
            print(f"{service} is {status}")
        else:
            print(f"{service} is {status}")


check_service(details)