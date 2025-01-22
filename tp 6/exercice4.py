class NegativeAgeError(Exception):
    def __init__(self, message="L'âge ne peut pas etre negatif."):
        super().__init__(message)

def set_age(age):
    if age < 0:
        raise NegativeAgeError(f"Erreur : L'âge ({age}) est invalide.")
    print(f"L'âge est {age} ans.")


try:
    set_age(-5)
except NegativeAgeError as e:
    print(e)
