liste = [1, 43, 8, -23, 12, -67, 42, -8, 21, -12, -42, -61, 8, 17, 42]

liste=[abs(val) for val in liste]
for index, val in enumerate(liste):
  if liste.count(val) > 1:
    liste.pop(index)

liste.sort()

print(liste)
