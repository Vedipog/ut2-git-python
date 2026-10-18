# Ejercicio 6: suma de los números pares (for + continue)
limite = int(input("Suma los pares hasta: "))
suma = 0

for i in range(1, limite + 1):
    if i % 2 != 0:
        continue
    suma += i

print("La suma de los pares es:", suma)
