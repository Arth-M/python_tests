# from cartes_module import *
import cartes_module as cart_mod
import sys
print(sys.path)

cartes = cart_mod.all_cards()
# tuple_carte=[]
# final_cards = []
# for index,value in enumerate(cartes):
#   tuple_carte.append(value)
#   if index % 2==0:
#     final_cards.append(tuple(tuple_carte))
#     del tuple_carte

print(cartes)

def carte(number=0):
  all = cart_mod.all_cards()
  return all[number]

print(carte(51))
