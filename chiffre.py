t = 0
while t <= 9:
    print(t)
    if t % 2:
        print(t, "est divisible par 2")
    else:
        print(t, "n'est pas divisible par deux")
    t += 1

print(t, "est divisible par 2") if t % 2 else print(t, "n'est pas divisible par deux")


for number in range(0,9):
    match number:
        case 1:
            print("tu as trouvé le", number)
        case 3:
            print(f"Le nombre est maintenant {number}")
        case _:
            print("None of your business")
