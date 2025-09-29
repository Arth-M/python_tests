print("Hello world!")

texte = "Ouahh"
nombre = 10 + 2
concatenate = texte + " " + str(nombre) + " enfants ça fait beaucoup ! "
concatenate_2 = (
    texte
    + " "
    + str(nombre)
    + " enfants ça fait beaucoup ! "
    + texte
    + " "
    + str(nombre)
    + " enfants ça fait beaucoup ! "
)

compteur = 1
while compteur <= 5:
    print("Le compteur est à " + str(compteur))
    compteur += 1
print("Compteur mic drop")
print(concatenate)
concatenate3 = print(texte, nombre, "enfants ça fait beaucoup !")
print(type(concatenate))
print(type(concatenate3))

# variables en snake_case (minuscule et underscore)

# input va demander un input à l'utilisateur et l'entrer dans la
# variable d'origine
# first_input = input("Écris moi qq chose : \n")

# print("Tu m'as vraiment écrit : ", first_input.upper(), "?")

# supprimer la variable compteur
del compteur

import keyword

print("Mots réservés : ", keyword.kwlist)

list_null = ""
print(bool(list_null))
rien = None
faux = False
vrai = True

print("tests boolen et comparaisons")
print(rien or vrai)
print(rien and faux)
print(not rien)
print(rien == vrai)


# Exos opérations arithmétiques
print("\n \n exos arithmétiques")
print([abs(-12.3), abs(-2), abs(3.78)])
print([int(-12.3), int(-2), int(3.78)])
print(int("3"))
print([float(-12.3), float(-2), float(3.78)])
print(float("3"))
print([round(-12.3), round(3.4), round(3.5), round(3.51), round(3.14159265)])

print(round(3.14159265, 4))

print("\n \n exos logique")
print(2 == 2.0)
print(type(2) == type(2.0))
print(3 != 3.00000001)
print(5 > 4)
print(5 >= 5.0)
print(5 <= 5.0)
print(4 <= 5.0)

text_test = "Hello!"
print(text_test[1])
print(text_test[0:5:2])
print(len(text_test))

print("He" in text_test)
print("Hel" not in text_test)


# test string
print("\n \n tests string")
alphabet = "abcdefghijklmnopqrstuvwxyz"
print(alphabet[4])
string_multilignes = """
Il y a plusieurs couleurs dans l'arc en ciel.
J'aime les couleurs froides comme le violet ou l'indigo.
Et vous, quelle est votre couleur favorite ?"""
print(string_multilignes)
print("spam" + "egg")
print("spam", "egg")

# print("a\cz")
print("a\nz")
print("a\\z")
# print("a\z")
print(
    "a\
      z"
)
print("a'z")
print('a"z')
print("\a")
print("abc\b\bz")
print("rtu\bz")
print("abcdef\rART")
print("a\tz")
print("abc\tzyx")


# essai string 2
print("\n \n Nouvel essai string")
s = "abc"
t = "def"

print(s * 4)
s = alphabet
print([s[0], s[3], s[25]])
print([s[0:3], s[3:6], s[20:26]])
print([s[:3], s[20:]])
print([s[0:25:2], s[6:24:3]])
print(len(s))
