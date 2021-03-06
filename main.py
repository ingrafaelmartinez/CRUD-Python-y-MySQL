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
        curso = funciones.registrarCurso()
        try:
            dao.registrarCurso(curso)
        except:
            print("Ocurrió un error")
    elif opcion == 3:
        try:
            cursos = dao.listarCursos()
            if len(cursos) > 0:
                curso = funciones.actualizacionCurso(cursos)
                if curso:
                    dao.actualizarCurso(curso)
                else:
                    print("Código de curso a actualizar no encontrado...\n")
            else:
                print("No se encontraron registros de cursos.")
        except:
            print("Ocurrió un error")
    elif opcion == 4:
        try:
            cursos= dao.listarCursos()
            if len(cursos) > 0:
                codigoEliminar = funciones.cursoEliminar(cursos)
                if not(codigoEliminar == ""):
                    dao.eliminarCurso(codigoEliminar)
                else:
                    print("No se encontraron cursos con el código ingresado...\n")
            else:
                print("No se encontraron registros de cursos.")
        except:
            print("Ocurrió un error")
    else:
        print("Opción no válida...")


menuPrincipal()