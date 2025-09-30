alphabet = "abcdefghijklmnopqrstuvwxyz"

chaine = input('Entrez une chaîne de caractères')
sous_chaine = input('Entrez une sous-chaîne de caractères')

repetitions = chaine.count(sous_chaine)

j=0
positions=[]
for i in range(1,repetitions+1):
  position = chaine.find(sous_chaine,j)
  positions.append(position)
  j = position
  j+=1

print(repetitions)
print(positions)
