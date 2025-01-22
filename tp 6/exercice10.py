def lire_fichier_et_saisir_entier():
    while True:
        try:

            nom_fichier = input(" entrez le nom de fichier : ")
            with open(nom_fichier, "r") as fichier:
                contenu = fichier.read()
                print("Contenu de fichier :")
                print(contenu)
            
            
            while True:
                try:
                    entier = int(input("entrer un nombre entier : "))
                    print(f"le nombre est : {entier}")
                    return
                except ValueError:
                    print("Entrée invalide.")
        except FileNotFoundError:
            print("Fichier introuvable.")
        except Exception as e:
            print(f"Une erreur: {e}")

lire_fichier_et_saisir_entier()
