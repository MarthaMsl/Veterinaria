
'''
Calse: Conexión a Base de Datos
Autor: Martha Soto Luna
Matricula: 181803008
Fecha creación: 25/10/2022
Última fecha de modificación: 07/11/2022
Docente: Rebeca Rodríguez Huesca
Materia: Ingeniería de requisitos
Proyecto: Veterinaria
Versión: 2.0
'''
import pymysql

class Conexion():
    #Función para crear la conexion
    def CreateDBConnection(self, host, puerto, usuario, servidor,database,user,password):
        connection = pymysql.connect(host="localhost", port=3306, user="root", password="", db="veterinaria")
        return connection
        
    #Función para cerrar la conexion
    def closeDBConnection(self,connection): 
        try: 
            connection.close() 
        except pymysql.ProgrammingError as e: 
            print(e)
            
    def mostrarProductos(self):
        cursor = self.con.cursor()
        sql = "SELECT * FROM producto " 
        cursor.execute(sql)
        producto = cursor.fetchall()
        return producto
    def mostrarPersonal(self):
        cursor = self.con.cursor()
        sql = "SELECT * FROM personal " 
        cursor.execute(sql)
        personal = cursor.fetchall()
        return personal
            
    

if __name__ == "__main__":
    server = 'Luna-Pc'
    host = "localhost"
    port = 3306
    database = 'veterinaria' 
    username = "root" 
    password = '' 

    prueba = Conexion()
    c =prueba.CreateDBConnection(host, port, username, server,database,username,password)    
    cursor = c.cursor()

    print('Estoy Dentro de Productos')
    cursor.execute("SELECT * from  producto")
    row = cursor.fetchone() 
    while row: 
        print("idProducto=%d  nombreProducto=%s  precio=%s cantidadProducto=%s  descripcion=%s" % (row[0], row[1], row[2], row[3], row[4]))
        row = cursor.fetchone()
    print('Estoy Dentro de Personal')
    cursor.execute("SELECT * from  personal")
    row = cursor.fetchone() 
    while row: 
        print("idPersonal=%d  cargo=%s  nombre=%s correo=%s  telefono=%s" % (row[0], row[1], row[2], row[3], row[4]))
        row = cursor.fetchone()