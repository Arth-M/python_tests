i = 0
while i < 5:
  reponse = input("Alors comment ça va?").strip().lower()
  if reponse == 'oui':
    print("Affirmatif mon général")
  else:
    print("Négatif mon général")
  i += 1
