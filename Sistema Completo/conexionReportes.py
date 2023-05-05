import pymysql

#Calse: Menu principal de ventas
#Autor: Samuel Martinez Arenas
#Matricula: 181803022
#Fecha creación: 25/10/2022
#Última fecha de modificación: 27/10/2022
#Docente: Rebeca Rodríguez Huesca
#Materia: Ingeniería de requisitos
#Proyecto: Veterinaria 


class ConexionBD():
    def CreateDBConnection(self, host, puerto, usuario, servidor,database,user,password):
        connection = pymysql.connect(host="localhost", port=3306, user="root", password="", db="veterinaria")
        return connection

    def closeDBConnection(self,connection): 
        '''Take input connection and close the database connection''' 
        try: 
            connection.close() 
        except pymysql.ProgrammingError as e: 
            print(e)


if __name__ == "__main__":
    server = 'DESKTOP-CT5AG1B'
    host = "localhost"
    port = 3306
    database = 'veterinaria' 
    username = "root" 
    password = '' 
    prueba = ConexionBD()
    c =prueba.CreateDBConnection(host, port, username, server,database,username,password)    
    cursor = c.cursor()
    cursor.execute("SELECT * from  personal")
    row = cursor.fetchone() 
    while row: 
        print("idPersonal=%d  cargo=%s  nombre=%s  correo=%s  telefono=%d" % (row[0], row[1], row[2], row[3], row[4]))
   
        row = cursor.fetchone()