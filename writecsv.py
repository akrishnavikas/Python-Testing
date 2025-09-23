import csv

data=[["HDFS","Running"],["Hive","Running"],["Impala","Stopped"]]

with open("data.csv","w",newline="") as file:
    writer = csv.writer(file)
    writer.writerow(['Service','Status'])
    writer.writerows(data)


print("Done")
    