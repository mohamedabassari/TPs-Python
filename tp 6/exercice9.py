def get_positive_integer():
    while True:
        try:
    
            user_input = int(input("entrer un entier positif : "))
            if user_input > 0:
                return user_input
            else:
                print("Le nombre doit etre positif.")
        except ValueError:
            print("Entrer invalide")

nombre = get_positive_integer()
print(f"le nombre est : {nombre}")
