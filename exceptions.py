# il. faut séparer les gestions d'erreur petit à petit:
# 1 traitement, une gestion d'erreur,
# et on répète comme ça étape par étape pour une bonne gestion
# des erreurs et des exécutions

var = input("Entrez une valeur")
alphabet = "abcdefghijklmnopqrstuvwxyz"
i = True
while i:
    try:
        value = 42 / float(var)
        print(value)

        print(alphabet[int(var)])
        i = False

    except FloatingPointError as err:
        print(f"Float? t'es sûr? {err=}, {type(err)=}")
        var = input("Entrez une valeur")
    except ValueError as err:
        print(f"Oulha ce n'est pas la bonne valeur {err=}, {type(err)=}")
        var = input("Entrez une valeur")
    except ZeroDivisionError as err:
        print(f"Division par zéro impossible {err=}, {type(err)=}")
        var = input("Entrez une valeur")
    except TypeError as err:
        print(f"Type error: {err=}, {type(err)=}")
        var = input("Entrez une valeur")
    except IndexError as err:
        print(f"Mauvais index dans l'alphabet: {err=}, {type(err)=}")
        var = input("Entrez une valeur")

    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        var = input("Entrez une valeur")
        raise

    finally:
        print("Hey what else ?")
