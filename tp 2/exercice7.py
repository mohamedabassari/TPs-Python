class Livre:
    def __init__(self, titre, auteur, annee_publication):
        self.titre = titre
        self.auteur = auteur
        self.annee_publication = annee_publication

    def __str__(self):
        return f"'{self.titre}' par {self.auteur}, publié en {self.annee_publication}"


class Bibliotheque:
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)
        print(f"Le livre '{livre.titre}' a été ajouté.")

    def afficher_livres(self):
        if not self.livres:
            print("La bibliothèque est vide.")
        else:
            print("Livres dans la bibliothèque :")
            for livre in self.livres:
                print(f" - {livre}")


if __name__ == "__main__":
    livre1 = Livre("La Boîte à Merveilles", "Ahmed Sefrioui", 1954)
    livre2 = Livre("Antigone", "Jean Anouilh", 1944)

    ma_bibliotheque = Bibliotheque()

    ma_bibliotheque.ajouter_livre(livre1)
    ma_bibliotheque.ajouter_livre(livre2)

    ma_bibliotheque.afficher_livres()
