import sys

                #CALCUL DE LA MOYENNE
les_nombres = []
choix_menu = """Veillez entrer des nombres pour calculer leur moyenne
1 : Ajouter un nombre
2 : Afficher les nombres
3 : Calculer la moyenne
    -->> """

choix_numero = ["1", "2", "3"]
def LaMoyenne():
    while True:
        nombre_choisi = ""
        while nombre_choisi not in choix_numero:
            nombre_choisi = input(choix_menu)
            if nombre_choisi not in choix_numero:
                print("Veillez choisir dans la liste")
        if nombre_choisi == "1":
            ajout_nombre = input("Ecrire un nombre \n -->> ")
            ajout_nombre = int(ajout_nombre)
            les_nombres.append(ajout_nombre)
        elif nombre_choisi == "2":
            print(sorted(set(les_nombres)))
            print(" -->> NB: Ne prend pas en copmpte les nombres entrés plus d'une fois ")
        elif nombre_choisi == "3":
            resultat_moyenne = (sum(set(les_nombres)) / len(set(les_nombres)))
            affichage = "La moyenne de cette liste de nombre est egal à : "
            print(f"{affichage} {resultat_moyenne}")
            sys.exit()
            
        print("_" * 50)
LaMoyenne()