def process_input(user_input):
    try:
        value = int(user_input)
        result = 10 / value
        print(f"Result: {result}")
    except ValueError:
        print("Error: Input n'est pas entier.")
    except ZeroDivisionError:
        print("Error: Division sur 0 erreur.")


process_input("0")
process_input("AB")
process_input("21")