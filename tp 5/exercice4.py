import csv  

with open("C:/Users/Admin/Desktop/master/Python/TPs/tp 5/contacts.csv", "r") as fichier_csv:
    lecteur = csv.DictReader(fichier_csv)  
    for contact in lecteur:
       
        print(f"Nom : {contact['Nom']}, Age : {contact['Age']}, Ville : {contact['Ville']}")
