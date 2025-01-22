with open("phrases.txt", "w") as fichier:
    for i in range(1, 4):
        
        phrase = input(f"Entrez la phrase {i} : ")
        
        fichier.write(phrase + "\n")

print("Les phrases ont été enregistrées dans le fichier 'phrases.txt'.")
