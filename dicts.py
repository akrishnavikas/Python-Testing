data = {"hdfs": "running", "yarn": "stopped", "hive": "running"}

for service,status in data.items():
    if status=="running":
        print(service)
    else:
        pass
