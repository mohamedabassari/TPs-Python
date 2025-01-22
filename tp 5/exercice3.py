def ajouter_phrases():
    with open("phrases.txt", "a") as fichier:
        while True:
            phrase = input("Entrez une phrase à ajouter (ou tapez 'stop' pour arrêter) : ")
            if phrase.lower() == "stop":
                break
            fichier.write(phrase + "\n")
        print("Les phrases ont été ajoutées à 'phrases.txt'.")
while True:
    reponse = input("Souhaitez-vous ajouter des phrases à 'phrases.txt' ? (oui/non) : ").lower()
    if reponse == "oui":
        ajouter_phrases()
        break
    elif reponse == "non":
        print("Aucune modification n'a été apportée au fichier.")
        break
    else:
        print("Veuillez répondre par 'oui' ou 'non'.")
