
import pymysql
from pymysql.cursors import Cursor
from pymysql.err import Error


HOST = "localhost"
PORT = 3306
USER = "root"
PASSWORD = ""
DATABASE = "universidad"

class DAO():
    
    def __init__(self):
        try:
            self.conexion = pymysql.connect(host=HOST, port=PORT, user=USER, passwd=PASSWORD, db=DATABASE)
        except Error as ex:
            print("Error al intentar conectar a la base de datos: ", ex)
    

    def listarCursos(self):
        if self.conexion.open:
            try:
                cursor = self.conexion.cursor()
                cursor.execute(" SELECT * FROM cursos ORDER BY nombre ASC ")
                resultados = cursor.fetchall()
                return resultados
                
            except Error as ex:
                print("Error al intentar conectar a la base de datos: ", ex)

    
    def registrarCurso(self, curso):
        if self.conexion.open:
            try:
                cursor = self.conexion.cursor()
                query = " INSERT INTO cursos(codigo, nombre, creditos) VALUES('{0}', '{1}', '{2}') "
                cursor.execute(query.format(curso[0], curso[1], curso[2]))
                self.conexion.commit()
                print("¡Curso registrado exitosamente!\n")
            except Error as ex:
                self.conexion.rollback()
                print("Error al intentar conectar a la base de datos: ", ex)


    def actualizarCurso(self, curso):
        if self.conexion.open:
            try:
                cursor = self.conexion.cursor()
                query = " UPDATE cursos SET nombre = '{0}', creditos = {1} WHERE codigo = '{2}' "
                cursor.execute(query.format(curso[1], curso[2], curso[0]))
                self.conexion.commit()
                print("¡Curso actualizado exitosamente!\n")
            except Error as ex:
                self.conexion.rollback()
                print("Error al intentar conectar a la base de datos: ", ex)


    def eliminarCurso(self, codigoCursoEliminar):
        if self.conexion.open:
            try:
                cursor = self.conexion.cursor()
                query = " DELETE FROM cursos WHERE codigo = '{0}' "
                cursor.execute(query.format(codigoCursoEliminar))
                self.conexion.commit()
                print("¡Curso eliminado exitosamente!\n")
            except Error as ex:
                self.conexion.rollback()
                print("Error al intentar conectar a la base de datos: ", ex)