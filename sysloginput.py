import sys

filename = sys.argv[1]

with open(filename,"r") as logfile:
    log_data=logfile.readlines()


print(len(log_data))