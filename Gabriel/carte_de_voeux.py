message = ["Joyeux Noël", "Joyeux Anniversaire", "Bonne Fête"]
for ind, valeur in enumerate(message):
    print(str(ind + 1) + " " + valeur)
choix = input("Choisissez un numéro de voeux dans cette liste: ")
if choix == "1":
    print(message[0])
elif choix == "2":
    print(message[1])
elif choix == "3":
    print(message[2])
else:
    print("il n'y a pas de voeux associé à ce numéro")
