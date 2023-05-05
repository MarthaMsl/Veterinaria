'''
Clase: Consultar Personal
Autor: Martha Soto Luna
Matricula: 181803008
Fecha creación: 07/11/2022
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
from BrowsPersonal import Ui_VentanaConsultarPersonal
from ConexionDB import Conexion


class ventanaConsultar(QMainWindow):
    def __init__(self):
        #Llamando a la interfáz
        super(ventanaConsultar, self).__init__()
        self.ui = Ui_VentanaConsultarPersonal()
        self.ui.setupUi(self)

        #Establece la conexion con la base de datos 
        self.c = Conexion()

        # Botones para dirigirse a las funciones
        self.ui.pushButton_volver.clicked.connect(self.salir)

        self.ui.tableConsultaPers.setColumnWidth(0,98)
        self.ui.tableConsultaPers.setColumnWidth(1,100)
        self.ui.tableConsultaPers.setColumnWidth(2,98)
        self.ui.tableConsultaPers.setColumnWidth(3,98)
        
        
        datos = self.c.mostrarPersonal()
        print(datos)
        i = len(datos)
        self.ui.tableConsultaPers.setRowCount(i) 
        tablerow = 0

        for row in datos:
            
            nombre = row[2]
            NOMBRE = str(nombre)

            cargo = row[1]
            CARGO = str(cargo)

            correo = row[3]
            CORREO = str(correo)

            telefono = row[4]
            TELEFONO = str(telefono)
            

            self.ui.tableConsultaPers.setItem(tablerow,0,QtWidgets.QTableWidgetItem(NOMBRE))			
            self.ui.tableConsultaPers.setItem(tablerow,1,QtWidgets.QTableWidgetItem(CARGO))
            self.ui.tableConsultaPers.setItem(tablerow,2,QtWidgets.QTableWidgetItem(CORREO))
            self.ui.tableConsultaPers.setItem(tablerow,3,QtWidgets.QTableWidgetItem(TELEFONO))
            tablerow +=1
    
        

    #Funcion volver al menú       
    def salir(self):
        self.hide()

if __name__ == '__main__':
    app = QApplication([])
    main = ventanaConsultar()
    main.show()
    sys.exit(app.exec())