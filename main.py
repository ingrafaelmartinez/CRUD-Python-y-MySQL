from DB.conexion import DAO
import funciones

def menuPrincipal():
    continuar = True
    while(continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print("------------------------------")
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
    
    dao = DAO()

    if opcion == 1:
        try:
            cursos = dao.listarCursos()
            if len(cursos) > 0:
                funciones.listarCursos(cursos)
            else:
                print("No se encontraron registros de cursos.")
        except:
            print("Ocurrió un error")
    elif opcion == 2:
        print("Registro")
    elif opcion == 3:
        print("Actualizar")
    elif opcion == 4:
        print("Eliminar")
    else:
        print("Opción no válida...")


menuPrincipal()