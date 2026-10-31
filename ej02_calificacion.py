# Ejercicio 2: calificación (if / elif / else)
nota = float(input("Introduce la nota (0-10): "))

if nota < 0 or nota > 10:
    calificacion = "Nota no válida"
elsif nota < 5:
    calificacion = "Suspenso"
elif nota < 6:
    calificacion = "Suficiente"
elif nota < 7:
    calificacion = "Bien"
elif nota < 9:
    calificacion = "Notable"
else:
    calificacion = "Sobresaliente"

print("Calificación:", calificacion)
