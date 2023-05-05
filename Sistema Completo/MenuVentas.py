'''
Clase: Menu principal de Ventas
Autor: Martha Soto Luna
Matricula: 181803008
Fecha creación: 25/10/2022
Última fecha de modificación: 27/10/2022
Docente: Rebeca Rodríguez Huesca
Materia: Ingeniería de requisitos
Proyecto: Veterinaria
Versión: 2.0
'''


from ast import Delete
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from EliminarProducto import ventanaEliminar
from SalesMain import Ui_MenuVentas
from AgregarVenta import OtraVenta
from ConsultarVenta import ventanaConsultar

class ventanaPrincipalVent(QMainWindow):
    def __init__(self):
        super(ventanaPrincipalVent, self).__init__()
        self.ui = Ui_MenuVentas()
        self.ui.setupUi(self)

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

        
    def salir(self):
        self.hide()
        

if __name__ == '__main__':
    app = QApplication([])
    main = ventanaPrincipalVent()
    main.show()
    sys.exit(app.exec())
