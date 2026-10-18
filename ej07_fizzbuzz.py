# Ejercicio 7: FizzBuzz (for + if/elif/else)
limite = int(input("¿Hasta qué número? "))
for i in range(1, limite + 1):
    if i % 15 == 0:
        print("¡FizzBuzz!")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
print("Fin")