"""test python interpreter"""

import sys

nombre = 1
chaine = 'c'
liste=[1]

print('Taille de int:',sys.getsizeof(nombre))
print('Taille de str:',sys.getsizeof(chaine))
print('Taille de liste:',sys.getsizeof(liste))

i=0
while i < 10000:
  nombre *= 10
  chaine += 'c'
  liste.append(1)
  i+=1


print('Taille de int:',sys.getsizeof(nombre))
print('Taille de str:',sys.getsizeof(chaine))
print('Taille de liste:',sys.getsizeof(liste))
