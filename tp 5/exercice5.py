import json

etudiants = {
    "etudiants": [
        {"nom": "Abdellah", "age": 21, "note": 15.5},
        {"nom": "Abdelghani", "age": 20, "note": 14.0},
        {"nom": "Mohamed", "age": 21, "note": 12.8},
    ]
}

with open("etudiants.json", "w", encoding="utf-8") as fichier_json:
    json.dump(etudiants, fichier_json, indent=4, ensure_ascii=False)
print("Les données des étudiants ont été enregistrées dans 'etudiants.json'.")

with open("etudiants.json", "r", encoding="utf-8") as fichier_json:
    donnees = json.load(fichier_json)  

    print("\nInformations des étudiants :")
    for etudiant in donnees["etudiants"]:
        print(f"Nom : {etudiant['nom']}, Âge : {etudiant['age']}, Note : {etudiant['note']}")
