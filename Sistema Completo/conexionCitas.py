#Clase: Conexion Cita
#Autor: Samuel Martinez Arenas
#Matricula: 181803022
#Fecha creación: 10/11/2022
#Última fecha de modificación: 27/10/2022
#Docente: Rebeca Rodríguez Huesca
#Materia: Ingeniería de requisitos
#Proyecto: Veterinaria

import pymysql

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
    
    def consult_Personal(self):
        cursor = self.conexion.cursor()
        sql = "SELECT nombre FROM personal " 
        cursor.execute(sql)
        per = cursor.fetchall()
        return per


if __name__ == "__main__": 
    
    server = 'Familia Martuin'
    host = "localhost"
    port = 3306
    database = 'veterinaria' 
    username = "root" 
    password = '' 

    