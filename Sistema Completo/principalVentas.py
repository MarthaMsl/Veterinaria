#Calse: Menu principal de ventas
#Autor: Samuel Martinez Arenas
#Matricula: 181803022
#Fecha creación: 25/10/2022
#Última fecha de modificación: 27/10/2022
#Docente: Rebeca Rodríguez Huesca
#Materia: Ingeniería de requisitos
#Proyecto: Veterinaria


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit
from PyQt5.uic import loadUi
from PyQt5 import uic, QtWidgets
import pymysql

#importando Reporte
from MenuVentas import Ui_MenuVentas
from reportes import ventanaGenera
from AgregarVenta import OtraVenta
from ConsultarVenta import ventanaConsultar


class principalVenta(QMainWindow):
    def __init__(self):
        super(principalVenta, self).__init__()
        self.ui = Ui_MenuVentas()
        self.ui.setupUi(self)
       
        self.ui.pushButton_ReportVentas.clicked.connect(self.gReporte)
        self.agreg = ventanaGenera()


        self.ui.pushButton_Back.clicked.connect(self.salir)
        self.ui.pushButton_AddVenta.clicked.connect(self.VentanaAgregarV)
        self.ad = OtraVenta()

        self.ui.pushButton_consultVenta.clicked.connect(self.consultar)
        self.brows = ventanaConsultar()

       

    #Funciones para que los botones muestren las interfaces de VENTAS
    
    def VentanaAgregarV(self):
        self.ad.show()

    def consultar(self):
        self.brows.show()
    def gReporte(self):
        self.agreg.show()


    #Funcion que cierra la ventana mostrada        
    def salir(self):
        confirm = QMessageBox.question(self, 'Mensaje', "¿Quieres salir de la ventana?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if confirm == QMessageBox.Yes:
            self.hide()

        

if __name__ == '__main__':
    app = QApplication([])
    main = principalVenta()
    main.show()
    sys.exit(app.exec())