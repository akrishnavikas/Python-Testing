usage = int(input("Enter the usage percentage: "))

if usage >=80:
    print("High Cluster Utilisation")
elif usage >=60:
    print("Usage is moderate")
else:
    print("Usage is low")
