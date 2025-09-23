import os
print(os.getcwd())

path = os.getcwd()

files = os.listdir(path)

print(files)
print(type(files))