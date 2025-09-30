prise_en_charge=2

# Tarifs département
A=0.91
B=1.35
C=1.82
D=2.7

def course(distance=0,tarif=C,minimum=prise_en_charge,supplement=0):
  return (distance * tarif) + minimum + supplement

prix = course(distance=52, tarif=C)
print(prix)
prix = course(distance=52, tarif=C, supplement=2)
print(prix)
prix = course(distance=52, tarif=A)
print(prix)
prix = course(distance=40, tarif=A)
print(prix)
prix = course(distance=60, tarif=A)
print(prix)
