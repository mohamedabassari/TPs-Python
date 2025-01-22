def read_file(filename):
    try:
        
        fichier = open(filename, "r")
        contenu = fichier.read()
        print("Contenu du fichier :")
        print(contenu)
    except FileNotFoundError:
        
        print(f"Erreur : Le fichier '{filename}' n'existe pas.")
    finally:

        try:
            fichier.close()
        except NameError:
            pass  

read_file("exemple.txt")  
