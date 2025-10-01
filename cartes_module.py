import random

def couleur(nombre=''):
  carte=''
  match nombre:
    case 1:
      carte="pique"
    case 2:
      carte="coeur"
    case 3:
      carte="trèfle"
    case 4:
      carte="carreau"
  return carte

def valeur(nombre=''):
  carte=''
  match nombre:
    case 1:
      carte="As"
    case 11:
      carte="Valet"
    case 12:
      carte="Dame"
    case 13:
      carte="Roi"
  if nombre>=2 and nombre<=10:
    carte=nombre
  return carte

def all_cards():
  carte1=''
  carte2=''
  cartes=[]
  for i in range(1,5):
    carte2=couleur(i)
    for j in range(1,14):
      carte1=valeur(j)
      if __name__== "__main__":
        cartes+=[f'{carte1:<35} {carte2:>5}']
      else:
        cartes.append((carte1,carte2))
  return cartes


if __name__== "__main__":
  cartes = all_cards()
  # for i in cartes:
  #   print(i)
  print(cartes[11])
  print(cartes[random.randint(0, 51)])
