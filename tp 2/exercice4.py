class Personne:
    def __init__(self,nom,prenom,age):
        self.nom=nom
        self.prenom=prenom
        self.age=age

    def se_presente(self):
        print(f"nom est {self.nom} le prenom est {self.prenom} l'age est {self.age}")

class Etudiant(Personne) :
    def __init__(self, nom, prenom, age,matricule):
        super().__init__(nom, prenom, age)       
        self.matricule=matricule

    def etudie(self):
        print(f"matricule {self.matricule} est etudiant")
    




p1 = Personne("abdellah","Mohamed",21)
p1.se_presente()
E1 = Etudiant("adil","aboubaker",18,"D137280")
E1.se_presente()
E1.etudie()