
'''
Calse: Conexión a Base de Datos
Autor: Martha Soto Luna
Matricula: 181803008
Fecha creación: 25/10/2022
Docente: Rebeca Rodríguez Huesca
Materia: Ingeniería de requisitos
Proyecto: Veterinaria
Versión: 2.0
'''
import pymysql

class Conexion():
    #Función para crear la conexion

    def __init__(self):
        self.connection = pymysql.connect(host="localhost", port=3306, user="root", password="", db="veterinaria")
        
        
    #Función para cerrar la conexion
    def closeDBConnection(self): 
        try: 
            self.connection.close() 
        except pymysql.ProgrammingError as e: 
            print(e)
            
    def mostrarProductos(self):
        cursor = self.connection.cursor()
        sql = "SELECT * FROM producto " 
        cursor.execute(sql)
        producto = cursor.fetchall()
        return producto
    def mostrarPersonal(self):
        cursor = self.connection.cursor()
        sql = "SELECT * FROM personal " 
        cursor.execute(sql)
        personal = cursor.fetchall()
        return personal
    
    def mostrarVenta(self):
        cursor = self.connection.cursor()
        sql = "SELECT idVenta, importeTotal FROM ventas " 
        cursor.execute(sql)
        ventas = cursor.fetchall()
        return ventas
    def mostrarDetalle(self):
        cursor = self.connection.cursor()
        sql = "SELECT * FROM detalle_ventas " 
        cursor.execute(sql)
        detalle = cursor.fetchall()
        return detalle
    
            
    

if __name__ == "__main__":
    server = 'Luna-Pc'
    host = "localhost"
    port = 3306
    database = 'veterinaria' 
    username = "root" 
    password = '' 

    prueba = Conexion()
    print('Estoy Dentro de Productos')
    print(prueba.mostrarProductos())
    
    print('Estoy Dentro de Personal')
    print(prueba.mostrarPersonal)