try:
    with open("inexistant.txt", "r") as fichier:
        contenu = fichier.read()
        print("Contenu du fichier :")
        print(contenu)
except FileNotFoundError:
    print("Erreur : Le fichier 'inexistant.txt' n'existe pas.")
