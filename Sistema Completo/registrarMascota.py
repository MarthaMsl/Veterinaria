import sys
from agregarMascota import Ui_agregarMascota
from conexionMascotas import ConexionBD
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit
import time

from PyQt5 import QtCore, QtGui, QtWidgets
#Calse: Registrar Mascota
#Autor: Samuel Martinez Arenas
#Matricula: 181803022
#Fecha creación: 25/10/2022
#Última fecha de modificación: 27/10/2022
#Docente: Rebeca Rodríguez Huesca
#Materia: Ingeniería de requisitos
#Proyecto: Veterinaria

class registrarMascota(QMainWindow):
    def __init__(self):
        super(registrarMascota, self).__init__()
        self.ui=Ui_agregarMascota()
        self.ui.setupUi(self)
        self.con=ConexionBD()
        self.conne=self.con.CreateDBConnection("localhost",3306, "root", 'Familia Martuin', 'veterinaria', "root", "")
        self.cursor=self.conne.cursor()
        self.ui.registrar.clicked.connect(self.agregar_mascota)
        self.ui.volver.clicked.connect(self.Salir)
        
    
    def agregar_mascota(self):
        mascota=self.ui.nomMascota.text()
        dueno=self.ui.nomDue.text()
        telefono=self.ui.telefono.text()
        email=self.ui.correo.text()
        
        if  (mascota!='') and (dueno!='')  and (telefono!='') and (email!=''):
            self.hide()
            #Ingresa a la función insertar
            sql="INSERT INTO mascota (nombreMascota, nombre_Dueno, telefono_Dueno ,correo) values(%s,%s,%s,%s)"
            self.cursor.execute(sql,(mascota, dueno, telefono ,email ))
            self.conne.commit()
            
            infor = QMessageBox()
            infor.setIcon(QMessageBox.Information)
            infor.setWindowTitle('Información')
            infor.setText('Inserción exitosa')
            infor.setInformativeText('Pulse Ok para continuar')
            infor.setStandardButtons(QMessageBox.Ok)
            infor.setDefaultButton(QMessageBox.Ok)
            resu = infor.exec_()

            #Borra los datos de las líneas de texto, de forma que se puedan volver a ingresar datos
            self.ui.nomMascota.setText('')
            self.ui.nomDue.setText('')
            self.ui.telefono.setText('')
            self.ui.correo.setText('')
             
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

            #Borra los datos de las líneas de texto, de forma que se puedan volver a ingresar datos
            '''self.ui.nomMascota.setText('')
            self.ui.nomDue.setText('')
            self.ui.telefono.setText('')
            self.ui.correo.setText('')'''

    def Salir(self):
        confirm = QMessageBox.question(self, 'Mensaje', "¿Quieres salir de la ventana?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if confirm == QMessageBox.Yes:
            self.hide()

if __name__ =="__main__":
    app = QApplication([])
    mi_app = registrarMascota()
    mi_app.show()
    sys.exit(app.exec_())