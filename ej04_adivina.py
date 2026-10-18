# Ejercicio 4: adivina el número (while + break)
import random

secreto = random.randint(1, 20)
intentos = 0

while True:
    intento = int(input("Adivina el número (1-20): "))
    intentos += 1
    if intento == secreto:
        print(f"¡Acertaste en {intentos} intentos!")
        break
    elif intento < secreto:
        print("Es mayor")
    else:
        print("Es menor")
