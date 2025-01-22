def safe_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Erreur : Division par zero erreur.")
    else:
        print(f"Résultat : {result}")
    finally:
        print("La fonction est terminer.")

print("Test 1")
safe_division(10, 2)

print("Test 2")
safe_division(10, 0)
