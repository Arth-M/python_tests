nom = input("Entrez votre nom").strip()
prenom = input("Entrez votre prenom").strip()
departement = input("Entrez votre département").strip()
ville = input("Entrez votre ville").strip()

# cartes+=[f'{carte1} de {carte2}']

print(
    f"{prenom.lower().capitalize()} {nom.lower().capitalize()} {departement} {ville.lower().capitalize()}"
)
print(
    f"{prenom.lower().capitalize()}:{nom.lower().capitalize()}:{departement}:{ville.lower().capitalize()}"
)
print(
    f"{prenom.lower().capitalize()} {nom.lower().capitalize()} {departement} {ville.lower().capitalize()}!"
)
print(
    f"{prenom.lower().capitalize()}:{nom.lower().capitalize()}---{departement}|{ville.lower().capitalize()}!"
)
