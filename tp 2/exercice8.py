class Personne:
    def __init__(self,nom):
        self.nom=nom
        self.amis=[]
    def ajouter_amis(self,ami):
        if ami not in self.amis:
            self.amis.append(ami)
        else :
            print(f"{ami} est déjà dans la liste d'amis de {self.nom}.")
    def afficher_amis(self):
        if not self.amis:
            print(f"{self.nom} n'a pas encore d'amis.")
        else:
            print(f"Les amis de {self.nom} sont :")
            for ami in self.amis:
                print(f" - {ami}")


if __name__ == "__main__":
    
    personne = Personne("Mohamed")

personne.ajouter_amis("Mohamed")
personne.ajouter_amis("Abdellah")
personne.afficher_amis()        