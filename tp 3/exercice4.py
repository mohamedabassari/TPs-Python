class Produit:
    def __init__(self,nom,prix):
        self.__nom=nom
        if prix >= 0:
         self.__prix=prix
        else:
           print("le prix doit etre positif")
    def prix_avec_remise(self,remise):
        if self.__prix > 100:
            return self.__prix * (1 - remise / 100)
        return self.__prix
p1 = Produit("TV", 7500)
print(p1.prix_avec_remise(15))  