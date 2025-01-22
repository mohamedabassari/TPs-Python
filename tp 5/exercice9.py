
try:
   
    with open("exemple.txt", "r") as fichier:
        contenu = fichier.readlines()  


    total_lignes = len(contenu)


    total_mots = 0
    total_caracteres = 0
    for ligne in contenu:
        total_mots += len(ligne.split())  
        total_caracteres += len(ligne)   

    
    print("Statistiques du fichier :")
    print(f"- Nombre total de lignes : {total_lignes}")
    print(f"- Nombre total de mots : {total_mots}")
    print(f"- Nombre total de caractères : {total_caracteres}")

except FileNotFoundError:
    print("Erreur : Le fichier 'exemple.txt' n'existe pas.")
