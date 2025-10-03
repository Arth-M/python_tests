import csv

rotten_list = []
i = 0
two_thousand_list = []
j = 0
comedy_list = []

with open("movies.csv", newline="") as data:
    # use DictReader class to read columns nnames as keys of a dictionnary
    reader = csv.reader(data, delimiter=",")
    next(reader)

    for row in reader:
        if int(row[5]) > 50:
            rotten_list.append(row[0])
            i += 1
        if int(row[7]) == 2008:
            two_thousand_list.append(row[0])
            j += 1
        if row[1] == "Comedy":
            comedy_list.append(float(row[3]))

print("Nombre films note sup à 50%:", i)
for element in rotten_list:
    print(element)
print("\n \n \n")
print("Nombre films sortis en 2008:", j)
for element in two_thousand_list:
    print(element)
print("\n \n \n")

print("Moyenne audiences des films comédie:", sum(comedy_list) / len(comedy_list))
