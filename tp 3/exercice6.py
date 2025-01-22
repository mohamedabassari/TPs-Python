
class Produit:
    def __init__(self, nom, prix):
        self.nom = nom  
        self.prix = prix  
    def afficher_produit(self):
        print(f"Produit : {self.nom} et Prix : {self.prix} Dhs")

class Commande:
    def __init__(self, produit, quantite):
        self.produit = produit  
        self.quantite = quantite  

    def calculer_total(self):
        return self.produit.prix * self.quantite

    def afficher_commande(self):
        
        print(f"{self.quantite} x {self.produit.nom} = {self.calculer_total()} Dhs")

class Panier:
    def __init__(self):
        self.commandes = []  

    def ajouter_commande(self, commande):
        self.commandes.append(commande)
        print(f"Commande ajoutée : {commande.quantite} x {commande.produit.nom}")

    def calculer_total_panier(self):
        total = sum(commande.calculer_total() for commande in self.commandes)
        return total

    def afficher_panier(self):
        print("Contenu du panier :")
        if not self.commandes:
            print("Le panier est vide.")
        else:
            for commande in self.commandes:
                commande.afficher_commande()
            print(f"Total du panier : {self.calculer_total_panier()} Dhs")

produit1 = Produit("Laptop", 8000)
produit2 = Produit("Souris", 150)
produit3 = Produit("Clavier", 300)


commande1 = Commande(produit1, 1)  
commande2 = Commande(produit2, 2) 
commande3 = Commande(produit3, 1)  

panier = Panier()


panier.ajouter_commande(commande1)
panier.ajouter_commande(commande2)
panier.ajouter_commande(commande3)

panier.afficher_panier()
