while True:
  jour = input("Quel est le jour de la semaine ? \n")

  if "lundi" in jour.lower():
    print("Dommage ce n'est pas un super jour, réessayez!")
    break
  else:
    print("Bonne journée")
