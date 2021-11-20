
def menuPrincipal():
    print("...:::  MENÚ PRINCIPAL  :::...")
    print("1. Listar cursos")
    print("2. Registrar curso")
    print("3. Actualizar curso")
    print("4. Eliminar curso")
    print("5. SALIR")
    print("------------------------------")

    opcion = int(input("Seleccione una opción: "))

    if opcion < 1 or opcion > 5:
        print("Opción incorrecta, ingrese una opción correcta...")
    elif opcion == 5:
        print("¡Gracias por usar el sistema! Hasta la próxima")
    else:
        ejecutarOpcion(opcion)


def ejecutarOpcion(opcion):
    print("Haz seleccionado la opción: ", opcion)


menuPrincipal()