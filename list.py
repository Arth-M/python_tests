liste = [1, 43, 8, -23, 12, -67, 42, -8, 21, -12, -42, -61, 8, 17, 42]

liste2 = [abs(val) for val in liste]
# liste.sort()
# print(liste2)
set_test = set(liste2)
# crée un set: un set possède des valeurs uniques,
# au lieu de append il a la fonction add
# for index, val in enumerate(liste2):
#   if liste2.count(val) > 1:
#     liste2.pop(index)

print(set_test)
print(set_test)

print(dir(set_test))
# help(set.pop)

set2 = {abs(val) for val in liste2}
liste_finale = list(set2)
liste_finale.sort()
print(liste_finale)
