'''
Clase: Menu principal de personal
Autor: Martha Soto Luna
Matricula: 181803008
Fecha creación: 07/11/2022
Última fecha de modificación: 07/11/2022
Docente: Rebeca Rodríguez Huesca
Materia: Ingeniería de requisitos
Proyecto: Veterinaria
Versión: 2.0
'''


from ast import Delete
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from EliminarPersonal import ventanaEliminar
from PersonalMain import Ui_MenuPersonal
from AgregarPersonal import ventanaAgregar
from ConsultarPersonal import ventanaConsultar
from ModificarPersonal import ventanaModificar

class ventanaPrincipalPer(QMainWindow):
    def __init__(self):
        super(ventanaPrincipalPer, self).__init__()
        self.ui = Ui_MenuPersonal()
        self.ui.setupUi(self)

        self.ui.pushButton_Back.clicked.connect(self.salir)
        
        self.ui.pushButton_Add.clicked.connect(self.VentanaAgregarP)
        self.ad = ventanaAgregar()

        self.ui.pushButton_consult.clicked.connect(self.consultar)
        self.brows = ventanaConsultar()

        self.ui.pushButton_Moddify.clicked.connect(self.Vmodificar)
        self.up = ventanaModificar()

        self.ui.pushButton_Delete.clicked.connect(self.eliminar)
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
    main = ventanaPrincipalPer()
    main.show()
    sys.exit(app.exec())
