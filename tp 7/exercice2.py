import os
import datetime
import math


repertoire_courant = os.getcwd()  
print(f"Répertoire courant : {repertoire_courant}")

date_heure = datetime.datetime.now()  
print(f"Date et Heure actuelles : {date_heure}")

nombre = float(input("Entrer un nombre : "))


racine_carree = math.sqrt(nombre)

print(f"La racine carree de {nombre} est {racine_carree}")
