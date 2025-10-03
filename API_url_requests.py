"""Fichier avec tout ce qui est orienté web:
*Gestion des api et url
*mails
*logs
*pydoc pour créer la doc
python3 -m pydoc -b => génère un serveur local avec toute la doc
de base de python ainsi que la doc qu'on a créée pour tous les fichiers
python du current working directory"""

import json  # pour gérer des json
import io
import requests  # pour les API
import urllib.request  # pour scrapper
import smtplib  # pour les mails
import pprint  # pretty print
import logging  # pour créer les logs
from PIL import Image



# import django  # web framework python
import pydoc  # génère les documentations

# python3 -m pydoc -b => génère un serveur local avec toute la doc
# de base de python ainsi que la doc qu'on a créée

import datetime  # c'est assez évident non ?

# pip freeze dans interpréteur pyhton permet d'avoir
# toutes les dépendances del'environnement python directement
# on le met dans requirements.txt
# puis en faisant pip install -r requirements.txt
# conda va permettre de gérer de façon automatisée
# les environnements virtuels et les requirements


now1 = datetime.datetime.today()
now = datetime.date.today()
print(now)
back_then = datetime.date(1988, 5, 16)
ok_back = datetime.datetime.combine(back_then, datetime.time())

print(ok_back)

difference2 = (now1 - ok_back).days
difference = (now - back_then).days
print(difference)
print(difference2)

# nom = input("Entrez votre nom")
# prenom = input("Entrez votre prénom")
# age = input("Entrez votre âge")
# liste_interet_str = input("Entrez votre liste d'intérêts")
# liste_interet = [i.strip() for i in liste_interet2.split(",")]

# with open("profil.json", "w", encoding="utf-8") as json_file:
#     json_file.write(
#         json.dumps(
#             {"nom": nom, "prenom": prenom, "age": age, "liste_interet": liste_interet},
#             indent=2,
#         )
#     )

with open("profil.json", "r", encoding="utf-8") as json_file:
    data = json.load(json_file)

print(json.dumps(data, indent=4))

for key, value in data.items():
    print(key, ":", value)


# api requests with 'requests'

URL_GITHUB = "https://api.github.com"
response = requests.get(URL_GITHUB)
data = response.json()
print(response.status_code)
print(json.dumps(data, indent=4))


# url_chuck = 'https://api.chucknorris.io/jokes/random'
URL_CHUCK = "https://api.chucknorris.io/jokes/search"
parametres = {"query": "captain"}
headers = {...}
# response = requests.get(url_chuck, params=parametres, headers=)
response = requests.get(URL_CHUCK, params=parametres)
data = response.json()
print(response.status_code)
print(json.dumps(data, indent=4))
# print(data["value"])


URL_PRENOMS = "https://api.agify.io"
prenom = input("Entrez votre prénom").strip().lower()
params={"name":prenom}
response = requests.get(URL_PRENOMS, params=params)
print(response.status_code)
print(f'https://http.cat/{response.status_code}')
image_response = requests.get(f'https://http.cat/{response.status_code}')
image = Image.open(io.BytesIO(image_response.content))
image.show()
data = response.json()
print(json.dumps(data, indent=4))

print(data['age'])
