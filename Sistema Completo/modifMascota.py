#Calse: Modificar Mascotas
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
from PyQt5.QtWidgets import QTableWidgetItem
from modificarMascota import Ui_modificarMascota 
from conexionMascotas import ConexionBD

class actualizarMascota(QMainWindow):
    def __init__(self):
        super(actualizarMascota, self).__init__()
        self.ui = Ui_modificarMascota()
        self.ui.setupUi(self)
        self.c = ConexionBD()
        self.conn=self.c.CreateDBConnection("localhost", 3306, "root", 'Familia Martuin', 'veterinaria', "root", "")
        self.cursor = self.conn.cursor()
        self.ui.buscar.clicked.connect(self.consulta_mascota)
        self.ui.modificar.clicked.connect(self.Guardar)
        self.ui.volver.clicked.connect(self.Salir)


        self.ui.nomMascotaM.setText('')
        self.ui.nomDueM.setText('')
        self.ui.telefonoM.setText('')
        self.ui.correoM.setText('')
    
    def consulta_mascota(self, ide):
        busqueda = self.ui.idB.text()
        resultado = self.consultar(busqueda)
        if resultado==True:
            #self.hide()
            #Selecciona sus atributos y los muestra en la línea de texto
            query = "SELECT idMascota, nombreMascota, nombre_Dueno, telefono_Dueno, correo from mascota WHERE idMascota = '%s'" %busqueda
            self.cursor.execute(query)
            row = self.cursor.fetchone()
            if row != None:
                v = int(busqueda)
                if row[0]==v:
                    nombreMascota = str (row[1])        
                    nombre_Dueno = str (row[2])
                    telefono_Dueno = str (row[3])
                    correo = str (row[4])

                    self.ui.nomMascotaM.setText(nombreMascota )
                    self.ui.nomDueM.setText(nombre_Dueno)
                    self.ui.telefonoM.setText(telefono_Dueno)
                    self.ui.correoM.setText(correo)

    def consultar(self, ide):
        #Consulta a la base de datos que busca el ID insertado (ide)
        query = "SELECT idMascota FROM mascota WHERE idMascota = '%s'" % ide
        self.cursor.execute(query)
        row = self.cursor.fetchone()
        #Buscando el ID
        if row != None:
            #Se debe convertir el ID en entero, debido a que entró a la función como cadena de caracteres, para compararlo con los valores enteros de los ID en la BD.
            ide = int(ide)
            #Si encontró coincidencias devuelve True
            if row[0] == ide:
                  return True
            #De lo contrario, devuelve False
            else:
                return False
        else:
            #Si no existe el ID
            #Mu
            #Muestra una ventana indicando que no existe ese ID
            infor = QMessageBox()
            infor.setIcon(QMessageBox.Warning)
            infor.setWindowTitle('Advertencia')
            infor.setText('No existe una mascota con ese ID o no hay ningun dato ingresado')
            infor.setInformativeText('Favor de insertar otro ID o ingresar uno')
            infor.setStandardButtons(QMessageBox.Ok)
            infor.setDefaultButton(QMessageBox.Ok)
            resu = infor.exec_()
            self.ui.idB.setText('')
            return False
        #Termina la conexión con la BD
        self.c.closeDBConnection(self.conn)

    def Guardar(self):
        idMascota=self.ui.idB.text()
        nomMas=self.ui.nomMascotaM.text()
        nomDue=self.ui.nomDueM.text()
        telefono=self.ui.telefonoM.text()
        email=self.ui.correoM.text()

        #Si todos los datos están llenos
        if idMascota!='':
            #Actualiza los datos en la BD
            actualizar= "UPDATE mascota SET nombreMascota = %s WHERE idMascota = %s"
            val = (nomMas, idMascota)
            self.cursor.execute(actualizar,val)
            self.conn.commit()
            actualizar= "UPDATE mascota SET nombre_Dueno = %s WHERE idMascota = %s"
            val = (nomDue, idMascota)
            self.cursor.execute(actualizar, val)
            self.conn.commit()
            actualizar= "UPDATE mascota SET telefono_Dueno = %s WHERE idMascota = %s"
            val = (telefono, idMascota)
            self.cursor.execute(actualizar, val)
            self.conn.commit()
            actualizar= "UPDATE mascota SET correo = %s WHERE idMascota = %s"
            val = (email, idMascota)
            self.cursor.execute(actualizar, val)
            self.conn.commit()

            #Muestra una ventana que indica que los datos fueron actualizados
            infor = QMessageBox()
            infor.setIcon(QMessageBox.Information)
            infor.setWindowTitle('Información')
            infor.setText('Operación exitosa')
            infor.setInformativeText('Pulse Ok para continuar')
            infor.setStandardButtons(QMessageBox.Ok)
            infor.setDefaultButton(QMessageBox.Ok)
            resu = infor.exec_()
            #Borra los datos de las líneas de texto
            self.ui.idB.setText('')
            self.ui.nomMascotaM.setText('')
            self.ui.nomDueM.setText('')
            self.ui.telefonoM.setText('')
            self.ui.correoM.setText('')
            
        #Si al menos una línea de texto está vacía
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
            self.ui.nomMascotaM.setText('')
            self.ui.nomDueM.setText('')
            self.ui.telefonoM.setText('')
            self.ui.correoM.setText('')
    
    def Salir(self):
        confirm = QMessageBox.question(self, 'Mensaje', "¿Quieres salir de la ventana?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if confirm == QMessageBox.Yes:
            self.hide()

    
if __name__ == '__main__':
    app = QApplication([])
    main = actualizarMascota()
    main.show()
    sys.exit(app.exec())