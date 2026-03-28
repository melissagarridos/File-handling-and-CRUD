# sistema de estado diario del equipo

import os

archivo = "database.txt"

# -----------------------------
# guardar blocker (append)
# -----------------------------
def guardar_blocker():
    blocker = input("Escribe tu Daily Blocker: ")

    with open(archivo, "a") as file:
        file.write(blocker + "\n")

    print("Blocker guardado\n")


# -----------------------------
# mostrar blockers (read)
# -----------------------------
def mostrar_blockers():

    if os.path.exists(archivo):

        with open(archivo, "r") as file:
            lineas = file.readlines()

        if len(lineas) == 0:
            print("No hay blockers guardados\n")
        else:
            print("\n--- LISTA DE BLOCKERS ---")

            contador = 1
            for linea in lineas:
                print(contador, "-", linea.strip())
                contador += 1

            print()

    else:
        print("El archivo no existe, primero guarda un blocker\n")


# -----------------------------
# borrar archivo (overwrite)
# -----------------------------
def borrar_datos():

    if os.path.exists(archivo):

        opcion = input("⚠️ Esto borrará todo. ¿Seguro? (si/no): ")

        if opcion == "si":
            with open(archivo, "w") as file:
                file.write("")
            print("Datos eliminados\n")
        else:
            print("Operación cancelada\n")

    else:
        print("No hay archivo para borrar\n")


# -----------------------------
# menú principal
# -----------------------------
opcion = ""

while opcion != "4":

    print("----- TEAM DAILY STATUS -----")
    print("1. Guardar blocker")
    print("2. Mostrar blockers")
    print("3. Borrar datos")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        guardar_blocker()

    elif opcion == "2":
        mostrar_blockers()

    elif opcion == "3":
        borrar_datos()

    elif opcion == "4":
        print("Saliendo del sistema...")

    else:
        print("Opción inválida\n")


# -----------------------------
# ENGLISH PRACTICE
# -----------------------------

# Protocol Selection (3-C Rule)
# 1. I will reach out via Slack because the issue is urgent and blocks the workflow.
# 2. I will send an email if the problem needs formal documentation.
# 3. I will create a Jira ticket to track the issue and assign responsibility.
