# Ejercicio 2: calificación (if / elif / else)
nota = float(input("Introduce la nota (0-10): "))

if nota < 5:
    calificacion = "Suspenso"
elif nota < 7:
    calificacion = "Aprobado"
elif nota < 9:
    calificacion = "Notable"
else:
    calificacion = "Sobresaliente"

print("Calificación:", calificacion)
