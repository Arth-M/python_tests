while True:
  prenom = input("Quel est votre prénom ? \n")

  # if prenom == "Horatio" or prenom == "Mac" or prenom == "Gil":
  if prenom in ("Horatio", "Mac", "Gil"):
    print("Bravo vous avez un super prénom")
    break
  else:
    print("Dommage ce n'est pas un super prénom, réessayez!")
