#Calse: Menu principal de mascotas
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
#importando CLIENTES
from menumascota import Ui_menuMascota
from registrarMascota import registrarMascota
from consulMascota import consultarMascota
from borrarMascota import borrarMascota
from modifMascota import actualizarMascota


class principalMascotas(QMainWindow):
    def __init__(self):
        super(principalMascotas, self).__init__()
        self.ui = Ui_menuMascota()
        self.ui.setupUi(self)
       
        self.ui.pushButton_AddMascota.clicked.connect(self.registrarMasco)
        self.agreg = registrarMascota()

        self.ui.pushButton_consultMascota.clicked.connect(self.consultarMasco)
        self.consult = consultarMascota()

        self.ui.pushButton_DeleteMascota.clicked.connect(self.borrarMasco)
        self.modif = borrarMascota()

        self.ui.pushButton_ModdifyMascota.clicked.connect(self.actualizarMasco)
        self.delete = actualizarMascota()

        self.ui.pushButton_Back.clicked.connect(self.salir)
    #Funciones para que los botones muestren las interfaces de VENTAS
    def registrarMasco(self):
        self.agreg.show()

    def consultarMasco(self): 
        self.consult.show()

    def borrarMasco(self): 
        self.modif.show()

    def actualizarMasco(self): 
        self.delete.show()
    #Funcion que cierra la ventana mostrada        
    def salir(self):
        confirm = QMessageBox.question(self, 'Mensaje', "¿Quieres salir de la ventana?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if confirm == QMessageBox.Yes:
            self.hide()

        

if __name__ == '__main__':
    app = QApplication([])
    main = principalMascotas()
    main.show()
    sys.exit(app.exec())