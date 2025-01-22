def convert_to_int(value):
    try:
        return int(value)
    except ValueError:
        raise ValueError(f"La valeur '{value}' ne peut pas être convertie en entier.")

try:
    resultat = convert_to_int("123")
    resultat = convert_to_int("AB")  
    print(f"Conversion réussie : {resultat}")
except ValueError as e:
    print(f"Erreur : {e}")
