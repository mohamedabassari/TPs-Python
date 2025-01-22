import logging

logging.basicConfig(filename='error.log', level=logging.ERROR, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def log_error(message):
    logging.error(message)

def read_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            print("Contenu du fichier :\n", content)
    except FileNotFoundError:
        error_message = f"Erreur : Le fichier '{filename}' est introuvable."
        print(error_message)
        log_error(error_message)
    finally:
        print("Opération terminée.")

read_file("inexistant.txt")
