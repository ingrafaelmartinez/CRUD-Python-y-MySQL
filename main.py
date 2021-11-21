
def menuPrincipal():
    continuar = True
    while(continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print("...:::  MENÚ PRINCIPAL  :::...")
            print("1. Listar cursos")
            print("2. Registrar curso")
            print("3. Actualizar curso")
            print("4. Eliminar curso")
            print("5. SALIR")
            print("------------------------------")

            opcion = int(input("Seleccione una opción: "))

            if opcion < 1 or opcion > 5:
                print("¡ERROR! Opción incorrecta, ingrese una opción correcta... \n")
            elif opcion == 5:
                continuar = False
                print("¡Gracias por usar el sistema! Hasta la próxima \n")
                break
            else:
                opcionCorrecta = True
                ejecutarOpcion(opcion)


def ejecutarOpcion(opcion):
    print("Haz seleccionado la opción: ", opcion)


menuPrincipal()