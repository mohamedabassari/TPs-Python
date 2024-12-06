class Rectangle :
    def __init__(self,largeur,hauteur):
        self.largeur=largeur
        self.hauteur=hauteur
    def calculer_surface(self):
        print(f"{self.largeur*self.hauteur}")

    def calculer_perimetre(self):
        print(f"{(self.largeur*self.hauteur)/2}")

larg1=Rectangle(5,3)
larg1.calculer_surface()
larg1.calculer_perimetre()
       
