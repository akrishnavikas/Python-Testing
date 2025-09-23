#This code is used to print first five lines of a log file.

with open("cloudera-scm-server.log","r") as file:
    logs_data=file.readlines()


print(len(logs_data))

error = [line for line in logs_data if "ERROR" in line]

print(len(error))