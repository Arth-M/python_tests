texte = input("Entrez ce que vous voulez").strip()
print(texte)
if texte.isalnum():

  if texte.isalpha():
    print("C'est du texte à 100%")

  if texte.islower():
    print("C'est du texte à 100%")
  else:
    print("Il y a des majs et des mins")
elif texte.isdigit():
  print("C'est du texte")
else:
  print("Trop compliqué mec")
