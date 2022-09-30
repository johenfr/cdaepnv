texte_a = "{} container{} pour {}"
texte_b = "Aucun container n'est réservé pour {}"
liste = ["firmes :"]
acceuil = input("tapez a pour démarrer.Merci d'écrire en nombres et en minuscules \n")
if acceuil == "a":
    nbr_cont = int(input("combien voulez vous de containers? \n"))
    if nbr_cont == 0:
        nom_firme = input("à quel nom ou à quelle firme? \n")
        print(texte_b.format(nom_firme))
        liste.insert(1, nom_firme)
        print(liste)
    else:
        if nbr_cont != 1:
            singulier_pluriel = "s"
        else:
            singulier_pluriel = ""
        nom_firme_x = input("à quel nom ou à quelle firme? \n")
        print(texte_a.format(nbr_cont, singulier_pluriel, nom_firme_x))
        liste.insert(1, nom_firme_x)
        print(liste)
else:
    print("pardon?")
