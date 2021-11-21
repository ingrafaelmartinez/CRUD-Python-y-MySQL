def listarCursos(cursos):
    print("\nCursos: \n")
    contador = 1
    for cur in cursos:
        datos = "{0}. Código: {1} | Nombre: {2} ({3} Créditos)"
        print(datos.format(contador, cur[0], cur[1], cur[2]))
        contador = contador + 1
    print(" ")

def registrarCurso():
    codigo = int(input("Ingrese el código del curso: "))
    nombre = input("Ingrese el nombre del curso: ")
    creditos = int(input("Ingrese los créditos del curso: "))

    curso = (codigo, nombre, creditos)
    return curso