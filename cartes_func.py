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
    case 2:
      carte="2"
    case 3:
      carte="3"
    case 4:
      carte="4"
    case 5:
      carte="5"
    case 6:
      carte="6"
    case 7:
      carte="7"
    case 8:
      carte="8"
    case 9:
      carte="9"
    case 10:
      carte="10"
    case 11:
      carte="Valet"
    case 12:
      carte="Dame"
    case 13:
      carte="Roi"
  return carte

test_valeur = valeur(1)
test_couleur = couleur(3)
print(test_valeur, test_couleur)

test_valeur2 = valeur(11)
test_couleur2 = couleur(4)
print(test_valeur2, test_couleur2)
