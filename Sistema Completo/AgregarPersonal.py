'''
Clase: Agregar Personal
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

#Importando vista y modelo
from AddPersonal import Ui_VentanaAgregarPersonal
from ConexionBD1 import Conexion


class ventanaAgregar(QMainWindow):
    def __init__(self):
        #Llamando a la interfáz
        super(ventanaAgregar, self).__init__()
        self.ui = Ui_VentanaAgregarPersonal()
        self.ui.setupUi(self)

        #Establece la conexion con la base de datos 
        self.c = Conexion()
        self.conne=self.c.CreateDBConnection("localhost",3306, "root", 'Luna-Pc', 'veterinaria', "root", "")
        self.cursor=self.conne.cursor()

        # Botones para difigirse a las funciones
        self.ui.pushButton_registrar.clicked.connect(self.insert_personal)
        self.ui.pushButton_volver.clicked.connect(self.salir)
       

    #Funcion para poder registrar productos en la base de datos
    def insert_personal(self):
        #Obtiene los datos desde los line 
        nombre = self.ui.lineNomPersonal.text()
        cargo = self.ui.lineCargoPersonal.text()
        correo = self.ui.lineCorreoPersonal.text()
        telefono = self.ui.lineTelPersonal.text()

        # Verifica si todos los datos estan llenos
        if (nombre!='') and (cargo!='') and (correo!='') and (telefono!=''):
            sql="INSERT INTO personal (cargo, nombre, correo, telefono	) values(%s,%s,%s,%s)"
            self.cursor.execute(sql,(cargo, nombre, correo, telefono))
            self.conne.commit()

            #Muestra una ventana que indica que los datos fueron actualizados
            infor = QMessageBox()
            infor.setIcon(QMessageBox.Information)
            infor.setWindowTitle('Información')
            infor.setText('Operación exitosa')
            infor.setInformativeText('Pulse Ok para continuar')
            infor.setStandardButtons(QMessageBox.Ok)
            infor.setDefaultButton(QMessageBox.Ok)
            resu = infor.exec_()

            #Limpia los lineedit para un nuevo registro
            self.ui.lineNomPersonal.clear()
            self.ui.lineCargoPersonal.clear()
            self.ui.lineCorreoPersonal.clear()
            self.ui.lineTelPersonal.clear()
            

        else:
            #Muestra una ventana de advertencia cuando faltan líneas de texto por llenar
            info = QMessageBox()
            info.setIcon(QMessageBox.Warning)
            info.setWindowTitle('Advertencia')
            info.setText('Faltan datos por llenar')
            info.setInformativeText('Favor de llenar todos los datos')
            info.setStandardButtons(QMessageBox.Ok)
            info.setDefaultButton(QMessageBox.Ok)
            result = info.exec_()

     
    #Funcion volver al menú       
    def salir(self):
        confirm = QMessageBox.question(self, 'Mensaje', "¿Estás seguro de querer volver al menú?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if confirm == QMessageBox.Yes:
            self.hide()
            self.c.closeDBConnection(self.conne)

if __name__ == '__main__':
    app = QApplication([])
    main = ventanaAgregar()
    main.show()
    sys.exit(app.exec())