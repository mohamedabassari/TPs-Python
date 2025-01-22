class Vehicule:
    def __init__(self, marque, modele, annee):
        self.marque = marque         
        self.modele = modele         
        self.annee = annee            

    def afficher_info(self):
        print(f"Véhicule : {self.marque} {self.modele}, Année : {self.annee}")

class Moteur:
    def __init__(self, puissance, type_moteur):
        self.puissance = puissance    
        self.type_moteur = type_moteur 

    def afficher_moteur(self):
        print(f"Moteur : {self.type_moteur}, Puissance : {self.puissance} chevaux")

class Voiture(Vehicule, Moteur):
    def __init__(self, marque, modele, annee, puissance, type_moteur, nombre_de_places):
        Vehicule.__init__(self, marque, modele, annee)
        Moteur.__init__(self, puissance, type_moteur)
        self.nombre_de_places = nombre_de_places  

    def afficher_info(self):
        super().afficher_info()  
        self.afficher_moteur()   
        print(f"Nombre de places : {self.nombre_de_places}")

class Moto(Vehicule, Moteur):
    def __init__(self, marque, modele, annee, puissance, type_moteur, type_moto):
        Vehicule.__init__(self, marque, modele, annee)
        Moteur.__init__(self, puissance, type_moteur)
        self.type_moto = type_moto 

    def afficher_info(self):
        super().afficher_info() 
        self.afficher_moteur()   
        print(f"Type de moto : {self.type_moto}")

voiture = Voiture("Toyota", "Corolla", 2020, 130, "Essence", 5)


moto = Moto("Yamaha", "R1", 2021, 200, "Essence", "Sport")

print("Informations sur la voiture :")
voiture.afficher_info()

print("\nInformations sur la moto :")
moto.afficher_info()
