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
'''from menumascota import Ui_menuMascota
from registrarMascota import registrarMascota
from consulMascota import consultarMascota
from borrarMascota import borrarMascota
from modifMascota import actualizarMascota
'''

from MenuCitas import Ui_MenuCitas 
from agregarCita import ventanaCitas
from borrarCita import ventanaEliminar
from consultaCita import ventanaConsultarCita

class principalCita(QMainWindow):
    def __init__(self):
        super(principalCita, self).__init__()
        self.ui = Ui_MenuCitas()
        self.ui.setupUi(self)
       
        self.ui.pushButton_AddProducto.clicked.connect(self.registrarCita)
        self.agreg = ventanaCitas()

        self.ui.pushButton_consultProdcto.clicked.connect(self.consultarCita)
        self.consult = ventanaConsultarCita()

        self.ui.pushButton_DeleteProducto.clicked.connect(self.borrarMasco)
        self.modif = ventanaEliminar()

        self.ui.pushButton_Back.clicked.connect(self.salir)


    #Funciones para que los botones muestren las interfaces de VENTAS
    def registrarCita(self):
        self.agreg.show()

    def consultarCita(self): 
        self.consult.show()

    def borrarMasco(self): 
        self.modif.show()

    #Funcion que cierra la ventana mostrada        
    def salir(self):
        confirm = QMessageBox.question(self, 'Mensaje', "¿Quieres salir de la ventana?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if confirm == QMessageBox.Yes:
            self.hide()


if __name__ == '__main__':
    app = QApplication([])
    main = principalCita()
    main.show()
    sys.exit(app.exec())