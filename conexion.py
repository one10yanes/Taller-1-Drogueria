import mysql.connector
from mysql.connector import Error
from sqlite3 import *



class DAO():

    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                password='',
                db='drogueria'
            )
            if self.conexion.is_connected():
                print ("conexion exitosa")
        except Error as ex:
            print("Error al intentar la conexión: {0}".format(ex))
            


    def listarClientes(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM cliente ")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar la conexión a la BD al listar los Usuarios: {0}".format(ex))


    def crearClientes(self, clientes):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO cliente (clienteId, nomcliente, nroTelefono) VALUES ('{0}','{1}', '{2}')"
                cursor.execute(sql.format(clientes[0], clientes[1], clientes[2]))
                self.conexion.commit()
                print("¡Cliente Registrado!\n")
            except Error as ex:
                print("Error en BD al crear el cliente: {0}".format(ex))

    def actualizarClientes(self, clientes):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "UPDATE cliente SET nomcliente='{0}', nroTelefono='{1}' WHERE clienteId={2}"
                cursor.execute(sql.format(clientes[1], clientes[2], clientes[0]))
                self.conexion.commit()
                print("¡Cliente Actualizado!\n")
            except Error as ex:
                print("Error en BD al actualizar el cliente: {0}".format(ex))

    def eliminarClientes(self, idCliente):
         if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE FROM cliente WHERE clienteId = '{0}'"
                cursor.execute(sql.format(idCliente))
                self.conexion.commit()
                print("¡Cliente eliminado!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))


