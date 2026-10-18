# Ejercicio 3: tabla de multiplicar (for)
n = int(input("¿Qué tabla quieres? "))

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
