'''
Calse: Consultar Producto
Autor: Martha Soto Luna
Matricula: 181803008
Fecha creación: 25/10/2022
Última fecha de modificación: 07/11/2022
Docente: Rebeca Rodríguez Huesca
Materia: Ingeniería de requisitos
Proyecto: Veterinaria
Versión: 2.0
'''

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit, QTableWidgetItem, QDialog
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
#Importando vista y modelo
from BrowsProduct import Ui_VentanaConsultarProducto
from ConexionDB import Conexion


class ventanaConsultar(QMainWindow):
    def __init__(self):
        #Llamando a la interfáz
        super(ventanaConsultar, self).__init__()
        self.ui = Ui_VentanaConsultarProducto()
        self.ui.setupUi(self)

        #Establece la conexion con la base de datos 
        self.c = Conexion()

        # Botones para dirigirse a las funciones
        self.ui.pushButton_volver.clicked.connect(self.salir)

        self.ui.tableConsultaProd.setColumnWidth(0,98)
        self.ui.tableConsultaProd.setColumnWidth(1,100)
        self.ui.tableConsultaProd.setColumnWidth(2,98)
        self.ui.tableConsultaProd.setColumnWidth(3,98)
        
        
        datos = self.c.mostrarProductos()
        print(datos)
        i = len(datos)
        self.ui.tableConsultaProd.setRowCount(i) 
        tablerow = 0

        for row in datos:
            
            nombreProducto = row[1]
            NOMBRE = str(nombreProducto)

            precio = row[2]
            PRECIO = str(precio)

            cantidadProducto = row[3]
            CANTIDAD = str(cantidadProducto)

            descripcion = row[4]
            DESCRIPCION = str(descripcion)
            

            self.ui.tableConsultaProd.setItem(tablerow,0,QtWidgets.QTableWidgetItem(NOMBRE))			
            self.ui.tableConsultaProd.setItem(tablerow,1,QtWidgets.QTableWidgetItem(PRECIO))
            self.ui.tableConsultaProd.setItem(tablerow,2,QtWidgets.QTableWidgetItem(CANTIDAD))
            self.ui.tableConsultaProd.setItem(tablerow,3,QtWidgets.QTableWidgetItem(DESCRIPCION))
            tablerow +=1
    
        

    #Funcion volver al menú       
    def salir(self):
        self.hide()

if __name__ == '__main__':
    app = QApplication([])
    main = ventanaConsultar()
    main.show()
    sys.exit(app.exec())