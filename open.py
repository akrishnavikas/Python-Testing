
with open("cloudera-scm-server.log", 'r') as file:
    log_lines = file.readlines()

print(f"The length of log_lines is : {len(log_lines)}")

error_lines = [line for line in log_lines if "ERROR" in line]

print(f"The numeber of lines having error are : {len(error_lines)}")