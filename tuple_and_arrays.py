neveux = ("riri", "fifi", "loulou")
bande = ["donald", "mickey"]

bande.append("picsou")
print(bande)

bande2=bande.copy()

bande.append(neveux)
print(bande)

bande.insert(0,"daisy")
print(bande)

# index=bande.find("mickey")
bande.pop(2)
print(bande)

bande.sort(key=len)
print(bande)

bande.reverse()
print(bande)


bande2.extend(neveux)
print("bande2:", bande2)

for val in bande2:
  if val in neveux:
    print(val,": c'est un neveu")
  else:
    print(val,": ce n'est pas un neveu")
