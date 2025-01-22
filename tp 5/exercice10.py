import csv
import os

fichier_contacts = "contacts.csv"

def initialiser_fichier():
    if not os.path.exists(fichier_contacts):
        with open(fichier_contacts, mode="w", newline="") as fichier:
            writer = csv.writer(fichier)
            writer.writerow(["Nom", "Prénom", "Téléphone"]) 


def ajouter_contact():
    nom = input("Entrer le nom : ")
    prenom = input("Entrer le prénom : ")
    telephone = input("Entrer le numéro de téléphone : ")
    with open(fichier_contacts, mode="a", newline="") as fichier:
        writer = csv.writer(fichier)
        writer.writerow([nom, prenom, telephone])
    print("Contact ajouter.")


def afficher_contacts():
    try:
        with open(fichier_contacts, mode="r") as fichier:
            reader = csv.DictReader(fichier)
            print("\nListe des contacts :")
            for contact in reader:
                print(f"- {contact['Nom']} {contact['Prénom']} : {contact['Téléphone']}")
    except FileNotFoundError:
        print("Aucun contact.")


def rechercher_contact():
    nom_recherche = input("Entrez le nom à rechercher : ")
    trouve = False
    try:
        with open(fichier_contacts, mode="r") as fichier:
            reader = csv.DictReader(fichier)
            for contact in reader:
                if contact["Nom"].lower() == nom_recherche.lower():
                    print(f"Contact trouvé : {contact['Nom']} {contact['Prénom']} - {contact['Téléphone']}")
                    trouve = True
                    break
        if not trouve:
            print("Aucun contact.")
    except FileNotFoundError:
        print("Aucun contact ajouter.")


def supprimer_contact():
    nom_supp = input("Entrez le nom du contact à supprimer : ")
    contacts_restants = []
    trouve = False

    try:
        with open(fichier_contacts, mode="r") as fichier:
            reader = csv.DictReader(fichier)
            for contact in reader:
                if contact["Nom"].lower() != nom_supp.lower():
                    contacts_restants.append(contact)
                else:
                    trouve = True

        if trouve:
            with open(fichier_contacts, mode="w", newline="") as fichier:
                writer = csv.DictWriter(fichier, fieldnames=["Nom", "Prénom", "Téléphone"])
                writer.writeheader()
                writer.writerows(contacts_restants)
            print("Contact supprimé avec succès.")
        else:
            print("Aucun contact trouver .")

    except FileNotFoundError:
        print("Aucun contact ajouté.")


def menu_principal():
    initialiser_fichier()
    while True:
        print("\n=== MENU ===")
        print("1. Ajouter un contact")
        print("2. Afficher tous les contacts")
        print("3. Rechercher un contact")
        print("4. Supprimer un contact")
        print("5. Quitter")
        choix = input("Choisissez une option : ")

        if choix == "1":
            ajouter_contact()
        elif choix == "2":
            afficher_contacts()
        elif choix == "3":
            rechercher_contact()
        elif choix == "4":
            supprimer_contact()
        elif choix == "5":
            print("Au revoir !")
            break
        else:
            print("Option invalide. Veuillez réessayer.")

menu_principal()
