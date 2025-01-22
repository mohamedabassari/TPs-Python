import shutil
import os


with open("journal.txt", "w") as f:
    f.write("Ligne 1 : Bonjour\n")
    f.write("Ligne 2 : Python est super\n")

shutil.copy("journal.txt", "journal_copie.txt")
print("Le fichier journal.txt a été copié.")


if not os.path.exists("archives"):
    os.mkdir("archives")

shutil.move("journal_copie.txt", "archives/journal_copie.txt")
print("Le fichier journal_copie.txt a été déplacé dans le dossier 'archives'.")
