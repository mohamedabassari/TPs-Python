class Personne:
    def __init__(self,nom,prenom,age):
        self.__nom=nom
        self.__prenom=prenom
        self.__age=age
    def getNom(self):
        return(self.__nom)
    def setNom(self,new_nom):
        self.__nom=new_nom
    def getPrenom(self):
        return(self.__prenom)
    def setPrenom(self,new_Prenom):
        self.__prenom=new_Prenom
    def getAge(self):
        return(self.__age)
    def setAge(self,new_age):
        self.__age=new_age    
        

p1 = Personne("Mohamed","Abassari",21)
p2 = Personne("Imad","Elharchoui",21)
print(f"le nom est {p1.getNom()} le prenom est {p1.getPrenom()} l'age est {p1.getAge()}")
print(f"le nom est {p2.getNom()} le prenom est {p2.getPrenom()} l'age est {p2.getAge()}")
p1.setNom("Abdellah")
p1.setPrenom("Abequawi")
print(f"le nom est {p1.getNom()} le prenom est {p1.getPrenom()} l'age est{p1.getAge()}")
