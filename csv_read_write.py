"""Importer des data en csv et gérer les cas particuliers"""
import csv

rotten_list = []
two_thousand_list = []
comedy_list = []

with open("movies.csv", newline="") as data:
    # use DictReader class to read columns nnames as keys of a dictionnary
    reader = csv.reader(data, delimiter=",")
    next(reader)

    for row in reader:
        if int(row[5]) > 50:
            rotten_list.append(row[0])
        if int(row[7]) == 2008:
            two_thousand_list.append(row[0])
        if row[1].lower() == "comedy":
            comedy_list.append(float(row[3]))

print("Nombre films note sup à 50%:", len(rotten_list))

print(", ".join(rotten_list))
print("\n \n \n")
print("Nombre films sortis en 2008:", len(two_thousand_list))
print(", ".join(two_thousand_list))
print("\n \n \n")

print("Moyenne audiences des films comédie:", sum(comedy_list) / len(comedy_list))
