#Calse: Menu principal de mascotas
#Autor: Samuel Martinez Arenas
#Matricula: 181803022
#Fecha creación: 25/10/2022
#Última fecha de modificación: 27/10/2022
#Docente: Rebeca Rodríguez Huesca
#Materia: Ingeniería de requisitos
#Proyecto: Veterinaria


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from PyQt5 import uic, QtWidgets

from menuprincipalSistema import Ui_MainWindow 
from principalMascotas import principalMascotas
from principalCitas import principalCita
from principalVentas import principalVenta
from MenuProductos import ventanaPrincipal 
from MenuPersonal import ventanaPrincipalPer


class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_Mascotas.clicked.connect(self.abrirMenuMascotas)
        self.ui.pushButton_Citas.clicked.connect(self.abrirMenuCitas)
        self.ui.pushButton_Ventas.clicked.connect(self.abrirMenuVentas)

        self.mmascotas = principalMascotas()
        self.mcitas = principalCita()
        self.mventas = principalVenta() 

        self.ui.pushButton_Productos.clicked.connect(self.VentanaMenuProductos)
        self.prod = ventanaPrincipal()  

        self.ui.pushButton_Personal.clicked.connect(self.VentanaMenuPersonal)
        self.pers = ventanaPrincipalPer()


    # Esta funcion permite abrir la función de citas
    def abrirMenuMascotas(self):
        self.mmascotas.show()
    
    def abrirMenuCitas(self):
        self.mcitas.show()
    
    def abrirMenuVentas(self):
        self.mventas.show()
    
    def VentanaMenuProductos(self):
        self.prod.show()
    
    def VentanaMenuPersonal(self):
        self.pers.show()


    
       

if __name__ == '__main__':
    app = QApplication([])
    main = VentanaPrincipal()
    main.show()
    sys.exit(app.exec())