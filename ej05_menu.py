# Ejercicio 5: menú de opciones (match-case, Python 3.10+)
print("1. Saludar")
print("2. Despedirse")
print("3. Salir")

opcion = input("Elige una opción: ")

match opcion:
    case "1":
        print("¡Hola!")
    case "2":
        print("¡Adiós!")
    case "3":
        print("Saliendo...")
    case _:
        print("Opción no válida")
