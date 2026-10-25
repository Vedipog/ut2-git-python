# Cómo contribuir a ut2-git-python

Este repositorio reúne ocho ejercicios de estructuras de control en Python, hechos durante la práctica de Git de la UT2. Este documento explica cómo está organizado el trabajo, para que cualquiera que se incorpore pueda proponer cambios sin romper la versión que funciona.

## Requisitos

- **Python 3.10 o superior.** El ejercicio `ej05_menu.py` usa `match` / `case`, que no existe en versiones anteriores. El proyecto se ha probado con Python 3.14.
- **Git**, y una **clave SSH** añadida a tu cuenta de GitHub para poder subir ramas.
- Permiso de colaborador en el repositorio, que concede el propietario.

## Cómo clonar y ejecutar el proyecto

```bash
git clone git@github.com:Vedipog/ut2-git-python.git
cd ut2-git-python
python3 ej01_par_impar.py
```

Cada ejercicio es un programa independiente. Todos piden datos por teclado, salvo `ej07_fizzbuzz.py`, que solo pide el límite. En Windows, sin WSL, se ejecutan con `python` en lugar de `python3`.

## Estructura del repositorio

| Fichero | Qué contiene |
|---|---|
| `ej01_par_impar.py` | Dice si un número entero es par o impar (`if` / `else`) |
| `ej02_calificacion.py` | Convierte una nota numérica en calificación y rechaza notas fuera de 0-10 (`if` / `elif` / `else`) |
| `ej03_tabla_multiplicar.py` | Muestra la tabla de multiplicar de un número, alineada en columnas (`for`) |
| `ej04_adivina.py` | Juego de adivinar un número aleatorio del 1 al 20 (`while` + `break`) |
| `ej05_menu.py` | Menú de opciones (`match` / `case`) |
| `ej06_suma_pares.py` | Suma los números pares hasta un límite (`for` + `continue`) |
| `ej07_fizzbuzz.py` | FizzBuzz hasta el número que indique el usuario (`for` + `if` / `elif`) |
| `ej08_contrasena.py` | Pide una contraseña con tres intentos (`while` / `else`) |
| `README.md` | Presentación del proyecto y tabla de ejercicios |
| `.gitignore` | Ficheros que Git no debe guardar |

El `.gitignore` excluye `__pycache__/` y los `*.pyc`, porque los genera Python automáticamente al ejecutar los programas, y `notas.txt`, que son notas personales. Si generas ficheros temporales o propios, añádelos al `.gitignore` en lugar de subirlos.

## Flujo de ramas

`main` contiene siempre la versión que funciona, así que **nunca se trabaja directamente sobre ella**. Cada cambio se hace en una rama nueva, creada desde `main` actualizada, con un nombre corto que diga qué se va a hacer:

```bash
git switch main
git pull
git switch -c nombre-de-la-rama
```

Ejemplos de ramas que ya se han usado en el proyecto:

- `bucles`: ejercicios 3 y 4.
- `menu`: ejercicio 5.
- `validar-nota`: validación del rango de notas en el ejercicio 2.
- `suma-pares`: ejercicio 6.
- `contrasena`: ejercicio 8.
- `mejora-fizzbuzz`: cambio de estilo en el ejercicio 7.
- `mejora-readme`: primera Pull Request del proyecto (#1).

Cuando la rama se ha fusionado en `main`, se borra.

## Mensajes de commit

Cada commit sigue el formato `tipo: descripción`. La descripción dice qué cambia, en una línea corta. Si hace falta explicar el porqué, se deja una línea en blanco y se añade un párrafo.

| Tipo | Cuándo se usa | Ejemplo real del historial |
|---|---|---|
| `feat` | Un ejercicio nuevo o una funcionalidad nueva | `feat: ejercicio 8 contraseña (while/else)` |
| `fix` | Corrección de un error | `fix: ej02 elimina marcadores de conflicto` |
| `docs` | Cambios en la documentación o en comentarios | `docs: añade ej07 y ej08 al README` |
| `style` | Cambios de formato o de texto que no alteran el funcionamiento | `style: ej03 alinea la tabla` |
| `refactor` | Reorganizar código sin cambiar lo que hace | (todavía no se ha usado) |
| `test` | Pruebas | (todavía no se ha usado) |

Para deshacer un commit que ya está en GitHub se usa `git revert`, que crea un commit nuevo en lugar de borrar historia, como en `Revert "fix: ej05 mensaje de salida"`. Nunca se usa `git reset` sobre commits ya subidos.

## Cómo proponer un cambio

1. Actualiza `main` y crea una rama desde ella (ver «Flujo de ramas»).
2. Haz los cambios en commits pequeños, con el formato indicado arriba.
3. Ejecuta los ejercicios que hayas tocado y comprueba que funcionan.
4. Sube la rama: `git push -u origin nombre-de-la-rama`.
5. En GitHub, abre una Pull Request hacia `main`. En el título resume el cambio, y en la descripción explica qué has hecho y por qué.
6. Espera la revisión. Si te piden cambios, haz nuevos commits en la misma rama y súbelos con `git push`: la Pull Request se actualiza sola.
7. Cuando esté aprobada, se fusiona desde GitHub y se borra la rama. Después, en tu equipo: `git switch main` y `git pull`.

Si al fusionar aparece un conflicto, no basta con borrar los marcadores `<<<<<<<`, `=======` y `>>>>>>>`: hay que dejar el código combinado correctamente y ejecutar el programa antes de confirmar.

## Versiones

Las versiones se marcan con etiquetas anotadas:

| Etiqueta | Contenido |
|---|---|
| `v1.0` | Ejercicios 1 a 5 |
| `v2.0` | Ejercicios 1 a 8 |

Para crear una nueva: `git tag -a vX.Y -m "descripción"` y `git push origin --tags`.