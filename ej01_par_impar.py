# Ejercicio 1: par o impar (if / else)
# Autor: Compañero
while True:
    try:
        numero = int(input("Introduce un número entero: "))
        break
    except ValueError:
        print("Eso no es un número entero. Inténtalo de nuevo.")

if numero % 2 == 0:
    print(numero, "es par")
else:
    print(numero, "es impar")
