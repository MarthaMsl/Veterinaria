# Autor
# Samuel Martinez Arenas
# Matricula: 181803022
# Fecha: 27/10/2022
# Proyecto Final Veterinaria 
# Ingenieria de Requisitos - Rebeca Rodríguez Huesca

import pymysql

class Consultar_datos():

    def __init__(self):
        self.conexion  = pymysql.connect( host="localhost", port=3306, user="root", password="", db="veterinaria")
        #establece la conexion para mostrar citas
    def mostrar_personal(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM mascota " 
        cursor.execute(sql)
        personal = cursor.fetchall()
        return personal