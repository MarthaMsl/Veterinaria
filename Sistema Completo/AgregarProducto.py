'''
Clase: Agregar Productos
Autor: Martha Soto Luna
Matricula: 181803008
Fecha creación: 25/10/2022
Última fecha de modificación: 27/10/2022
Docente: Rebeca Rodríguez Huesca
Materia: Ingeniería de requisitos
Proyecto: Veterinaria
Versión: 2.0
'''

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit, QTableWidgetItem, QDialog

#Importando vista y modelo
from AddProduct import Ui_VentanaAgregarProducto
from ConexionBD1 import Conexion



class ventanaAgregar(QMainWindow):
    def __init__(self):
        #Llamando a la interfáz
        super(ventanaAgregar, self).__init__()
        self.ui = Ui_VentanaAgregarProducto()
        self.ui.setupUi(self)

        #Establece la conexion con la base de datos 
        self.c = Conexion()
        self.conne=self.c.CreateDBConnection("localhost",3306, "root", 'Jimena-PC', 'veterinaria', "root", "")
        self.cursor=self.conne.cursor()

        # Botones para difigirse a las funciones
        self.ui.pushButton_registrar.clicked.connect(self.insert_producto)
        self.ui.pushButton_volver.clicked.connect(self.salir)
       

    #Funcion para poder registrar productos en la base de datos
    def insert_producto(self):
        #Obtiene los datos desde los line y el spin
        nomProducto = self.ui.lineNomProducto.text()
        precio = self.ui.linePrecioProd.text()
        cantProduc = self.ui.spinBoxCantidad.value()
        description = self.ui.lineDescripcionProd.text()

        # Verifica si todos los datos estan llenos
        if (nomProducto!='') and (precio!='') and (cantProduc!='') and (description!=''):
            sql="INSERT INTO producto (nombreProducto, precio, cantidadProducto, descripcion	) values(%s,%s,%s,%s)"
            self.cursor.execute(sql,(nomProducto, precio, cantProduc, description))
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
            self.ui.lineNomProducto.clear()
            self.ui.linePrecioProd.clear()
            self.ui.spinBoxCantidad.clear()
            self.ui.lineDescripcionProd.clear()
            

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