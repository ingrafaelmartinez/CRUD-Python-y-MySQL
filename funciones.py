
def listarCursos(cursos):
    print("\nCursos: \n")
    contador = 1
    for cur in cursos:
        datos = "| {0}. Código: {1} | Nombre: {2} | ({3} Créditos) |"
        print("------------------------------------------------------------------------")
        print(datos.format(contador, cur[0], cur[1], cur[2]))
        contador = contador + 1
    print("------------------------------------------------------------------------")
    print(" ")


def registrarCurso():
    codigoCorrecto = False
    while(not codigoCorrecto):
        codigo = input("Ingrese el código del curso: ")
        if len(codigo) == 6:
            codigoCorrecto = True
        else:
            print("¡ERROR! Código incorrecto. Debe tener 6 dígitos.\n")

    nombre = input("Ingrese el nombre del curso: ")

    creditosCorrectos = False
    while(not creditosCorrectos):
        creditos = input("Ingrese los créditos del curso: ")
        if creditos.isnumeric():
            if (int(creditos) > 0):
                creditosCorrectos = True
                creditos = int(creditos)
            else:
                print("Los créditos deben ser mayor a 0.")
        else:
            print("¡ERROR, Valor no válido! Debe ingresar un número entero.")

    curso = (codigo, nombre, creditos)
    return curso


def actualizacionCurso(cursos):
    listarCursos(cursos)
    existeCodigo = False

    codigoActualizar = input("Ingrese el código del curso a actualizar: ")
    for cur in cursos:
        if cur[0] == codigoActualizar:
            existeCodigo = True
            break
    
    if existeCodigo:
        nombre = input("Ingrese el nombre del curso a modificar: ")

        creditosCorrectos = False
        while(not creditosCorrectos):
            creditos = input("Ingrese los créditos del curso a modificar: ")
            if creditos.isnumeric():
                if (int(creditos) > 0):
                    creditosCorrectos = True
                    creditos = int(creditos)
                else:
                    print("Los créditos deben ser mayor a 0.")
            else:
                print("¡ERROR, Valor no válido! Debe ingresar un número entero.")

        curso = (codigoActualizar, nombre, creditos)
        return curso


def cursoEliminar(cursos):
    listarCursos(cursos)
    existeCodigo = False

    codigoEliminar = input("Ingrese el código del curso a eliminar: ")
    for cur in cursos:
        if cur[0] == codigoEliminar:
            existeCodigo = True
            break

    if not existeCodigo:
        codigoEliminar = ""

    return codigoEliminar