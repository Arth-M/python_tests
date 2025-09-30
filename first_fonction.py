i = 5


def f(arg=i):
    print(arg)
    return arg*4


i = 6
# Les valeurs par défaut sont évaluées lors de la définition de la fonction dans la portée de la définition
# ici à la définition i=5
test = f()
print(test)
