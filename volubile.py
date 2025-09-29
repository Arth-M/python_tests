while True:
  phrase = input("Entrez une phrase que vous avez en tête :\n")
  longueur = len(phrase)
  if longueur < 10:
    print("Vous êtes concis!")
  elif longueur < 20:
    print("Vous pourriez être moins bavard!")
  else:
    print("Vous êtes une vraie pipelette! Ça suffit!")
    break
