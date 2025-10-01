import os, shutil

print(dir(os))

print(dir(shutil))


help(os)
help(shutil)

print(os.getcwd())
print(os.listdir("../../../../../Users/"))

shutil.copyfile("./mois.py", "./mois-copy.py")
os.remove("./mois-copy.py")
