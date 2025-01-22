
with open("exemple.txt", "r") as fichier:
    for numero, ligne in enumerate(fichier, start=1):
        print(f"Ligne {numero} : {ligne.strip()}")
