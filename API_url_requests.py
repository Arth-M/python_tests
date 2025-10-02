# import requests #pour les API
import urllib.request # pour scrapper
import smtplib # pour les mails
import pprint #pretty print
import logging # pour créer les logs

import datetime #c'est assez évident non ?

# pip freeze dans interpréteur pyhton permet d'avoir
# toutes les dépendances del'environnement python directement
# on le met dans requirements.txt
# puis en faisant pip install -r requirements.txt
# conda va permettre de gérer de façon automatisée
# les environnements virtuels et les requirements


now1 = datetime.datetime.today()
now = datetime.date.today()
print(now)
back_then = datetime.date(1988,5,16)
ok_back = datetime.datetime.combine(back_then, datetime.time())

print(ok_back)

difference2 = (now1-ok_back).days
difference = (now-back_then).days
print(difference)
print(difference2)
