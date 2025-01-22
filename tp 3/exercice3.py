from exercice1 import *

A=Cercle(4)
B=Rectangle(5,8)


def afficher_surface(formes):
    for forme in formes:
        print(f"La surface est : {forme.calculer_surface()}")

