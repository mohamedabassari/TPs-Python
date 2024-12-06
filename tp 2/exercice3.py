class CompteBancaire:
    def __init__(self,titulaire,solde):
        self.titulaire=titulaire
        self.solde=solde

    def deposer(self,montant):
        if montant>0:
            self.solde+=montant
        else :
            print("montant invalide")

    def retirer(self,montant):
        if montant>0:
            if self.solde>=montant:
                self.solde-=montant
            else :
                print("montant insuffisant")
        else:
            print("montant invalide") 

    def affichage_solde(self):
        print(f"monsieur {self.titulaire} solde {self.solde}")

compte=CompteBancaire("Abdellah",20000)
compte.affichage_solde()      
compte.deposer(2500)
compte.retirer(15000)
compte.affichage_solde()




        