import math

a = input("Entrez la longueur d'un côté du triangle rectangle")
b = input("Entrez l'autre longueur d'un côté du triangle rectangle")

# hypothenuse = format(math.sqrt(a*a + b*b),'.2f')
hypothenuse = format(math.hypot(float(a) + float(b)),'.2f')

print(hypothenuse)
