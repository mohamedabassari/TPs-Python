from abc import ABC 


class Forme(ABC):
    def calculer_surface(self):
        pass
class Cercle(Forme):
    def __init__(self,rayon):
        self.rayon=rayon

    def calculer_surface(self):
        return(self.rayon*2)*3,14
    
class Rectangle(Forme):
    def __init__(self,longeur,largeur):
        self.longuer=longeur
        self.largeur=largeur
    def calculer_surface(self):
        return self.largeur*self.longuer
    
A=Cercle(4)
B=Rectangle(5,9)
print(f"la surface de Cercle est {A.calculer_surface()} et la surface de rectangle {B.calculer_surface()}")
