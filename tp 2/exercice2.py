

class Voiture:
    # constructor
    def __init__(self,marque,modele,annee):
        self.marque=marque
        self.modele=modele
        self.annee=annee
    
    # les methodes
    def afficher_info(self):
        print(f"voiture {self.marque} {self.modele} {self.annee}")



# instanciation
voiture1=Voiture("BMW",2007,2025)
voiture1.afficher_info()        



        