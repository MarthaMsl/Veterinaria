import pymysql

#Autor: Samuel Martinez Arenas
#Revisor: Rebeca Rodríguez Huesca
#Descripción: Conecta la base de datos de MYSQL con las interfaces del programa
#Fecha: 27 de octubre de 2022

class ConexionBD():
    #Descripción: Función para crear la conexion SQL

    def CreateDBConnection(self, host, puerto, usuario, servidor,database,user,password):
        connection = pymysql.connect(host="localhost", port=3306, user="root", password="", db="veterinaria")
        return connection

    #Descripción: Función para cerrar la conexion

    def closeDBConnection(self,connection): 
        '''Take input connection and close the database connection''' 
        try: 
            connection.close() 
        except pymysql.ProgrammingError as e: 
            print(e)


if __name__ == "__main__":
    server = 'Familia Martuin'
    host = "localhost"
    port = 3306
    database = 'veterinaria' 
    username = "root" 
    password = '' 
    prueba = ConexionBD()
    c =prueba.CreateDBConnection(host, port, username, server, database, username, password)    
    cursor = c.cursor()
    cursor.execute("SELECT * from  mascota")
    row = cursor.fetchone() 
    while row: 
        print("idMascota=%s  nombreMascota=%s  nombre_Dueno=%s  telefono_Dueno=%s  correo=%s " % (row[0], row[1], row[2], row[3], row[4]))
   
        row = cursor.fetchone()