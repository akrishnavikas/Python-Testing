usage = int(input("Enter the cluster usage percentage: "))

def usage_checker(value, standard=80 ):
    if value > standard:
        print("High Utilisation")
    else:
        print("Low utilisation")


usage_checker(usage)