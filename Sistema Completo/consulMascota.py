import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit
from PyQt5.uic import loadUi
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from consultarMascotas import Ui_consultarMascota
from consulMasco import Consultar_datos

#Calse: Consultar Mascotas
#Autor: Samuel Martinez Arenas
#Matricula: 181803022
#Fecha creación: 25/10/2022
#Última fecha de modificación: 27/10/2022
#Docente: Rebeca Rodríguez Huesca
#Materia: Ingeniería de requisitos
#Proyecto: Veterinaria

class consultarMascota(QMainWindow):
    def __init__(self):
        super(consultarMascota, self).__init__()
        self.ui = Ui_consultarMascota()
        self.ui.setupUi(self)
        self.datosTotal = Consultar_datos()
       
        #self.ui.pushButton.clicked.connect(self.consulta_usuarios)
        self.consulta_usuarios()
        self.ui.volver.clicked.connect(self.Salir)

        self.ui.conMascota.setColumnWidth(0,98)
        self.ui.conMascota.setColumnWidth(1,100)
        self.ui.conMascota.setColumnWidth(2,98)
        self.ui.conMascota.setColumnWidth(3,98)
        self.ui.conMascota.setColumnWidth(4,98)
        
    def consulta_usuarios(self):
        datos = self.datosTotal.mostrar_personal()
        i = len(datos)
        self.ui.conMascota.setRowCount(i)
        tablerow = 0
		
        for row in datos:
            idMascota = row[0]
            IDMASCOTA = str(idMascota)
            nombreMascota = row[1]
            MASCOTA = str(nombreMascota)
            nombre_Dueno = row[2]
            DUENO = str(nombre_Dueno )
            telefono_Dueno = row[3]
            TELEFONO = str(telefono_Dueno)
            correo = row[4]
            CORREO = str(correo)
            

            self.ui.conMascota.setItem(tablerow,0,QtWidgets.QTableWidgetItem(IDMASCOTA))			
            self.ui.conMascota.setItem(tablerow,1,QtWidgets.QTableWidgetItem(MASCOTA))			
            self.ui.conMascota.setItem(tablerow,2,QtWidgets.QTableWidgetItem(DUENO))
            self.ui.conMascota.setItem(tablerow,4,QtWidgets.QTableWidgetItem(TELEFONO))			
            self.ui.conMascota.setItem(tablerow,3,QtWidgets.QTableWidgetItem(CORREO))			

            tablerow +=1

    def Salir(self):
        confirm = QMessageBox.question(self, 'Mensaje', "¿Quieres salir de la ventana?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if confirm == QMessageBox.Yes:
            self.hide()
     
if __name__ == '__main__':
    app = QApplication([])
    main = consultarMascota()
    main.show()
    sys.exit(app.exec())