class Employe:
    def __init__(self,nom,prenom,salaire):
       self.nom=nom
       self.prenom=prenom
       self.salaire=salaire
    def affiche_information(self):
        print(f"Nom : {self.nom} , prenom : {self.prenom} , Salaire : {self.salaire}") 
class Manager(Employe):
    def __init__(self, nom, prenom, salaire):
        super().__init__(nom, prenom, salaire)
        self.employes=[] 
    def ajouter_employe(self,employe) :
        self.employes.append(employe)
        print(f" {employe.nom} {employe.prenom} est ajouter")
    def affiche_employes(self):
        for empl in self.employes:
         print(f" {empl.nom} {empl.prenom}") 



manager = Manager("Abassari", "Mohamed", 3000)
employe1 = Employe("ayoube", "rida", 3000)
employe2 = Employe("hiba", "rida", 2000)

manager.ajouter_employe(employe1)
manager.ajouter_employe(employe2)

manager.affiche_employes() 