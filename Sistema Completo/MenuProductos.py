'''
Clase: Menu principal de productos
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
from ProductsMain import Ui_MainWindow
from AgregarProducto import ventanaAgregar
from ConsultarProducto import ventanaConsultar
from ModificarProducto import ventanaModificar

class ventanaPrincipal(QMainWindow):
    def __init__(self):
        super(ventanaPrincipal, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_Back.clicked.connect(self.salir)
        
        self.ui.pushButton_AddProducto.clicked.connect(self.VentanaAgregarP)
        self.ad = ventanaAgregar()

        self.ui.pushButton_consultProdcto.clicked.connect(self.consultar)
        self.brows = ventanaConsultar()

        self.ui.pushButton_ModdifyProducto.clicked.connect(self.Vmodificar)
        self.up = ventanaModificar()

        self.ui.pushButton_DeleteProducto.clicked.connect(self.eliminar)
        self.delete = ventanaEliminar()

    #Funciones para que los botones muestren las interfaces de VENTAS
    
    def VentanaAgregarP(self):
        self.ad.show()

    def consultar(self):
        self.brows.show()

    def Vmodificar(self):
        self.up.show()

    def eliminar(self):
        self.delete.show()
        
    def salir(self):
        self.hide()
        

if __name__ == '__main__':
    app = QApplication([])
    main = ventanaPrincipal()
    main.show()
    sys.exit(app.exec())
