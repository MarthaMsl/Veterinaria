#Calse: Eliminar Mascota
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

from eliminarMascota import Ui_eliminarMascota
from conexionMascotas import ConexionBD

class borrarMascota(QMainWindow):
    def __init__(self):
        super(borrarMascota, self).__init__()
        self.ui = Ui_eliminarMascota()
        self.ui.setupUi(self)
        self.c = ConexionBD()
        self.conn=self.c.CreateDBConnection("localhost", 3306, "root", 'Familia Martuin', 'veterinaria', "root", "")
        self.cursor = self.conn.cursor()
        self.ui.eliminar.clicked.connect(self.eliminar_mascota)
        self.ui.buscar.clicked.connect(self.consulta_mascota)
        self.ui.volver.clicked.connect(self.Salir)

        self.ui.nomMascotaE.setText('')
        self.ui.nomDueE.setText('')
        self.ui.telefonoE.setText('')
        self.ui.correoE.setText('')
    
    def consulta_mascota(self, ide):
        busqueda = self.ui.idB.text()
        resultado = self.consultar(busqueda)
        #self.ui.tableWidget.setRowCount(resultado)
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
        
                    nombreDueno = str (row[2])

                    telefono_Dueno = str (row[3])

                    correo = str (row[4])
                    self.ui.nomMascotaE.setText(nombreMascota)
                    self.ui.nomDueE.setText(nombreDueno)
                    self.ui.telefonoE.setText(telefono_Dueno)
                    self.ui.correoE.setText(correo)     

    def consultar(self, ide):
        #Consulta a la base de datos que busca el ID insertado (ide)
        query = "SELECT idMascota FROM mascota WHERE idMascota = '%s'" % ide
        self.cursor.execute(query)
        row = self.cursor.fetchone()
        #Buscando el ID
        if row != None:
            #Se debe convertir el ID en entero, debido a que entró a la función como cadena de caracteres, para compararlo con los valores enteros de los ID en la BD.
            ide = int(ide)
            #self.hide()
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
            infor.setText('No existe una mascota con ese ID o no hay ningún dato ingresado')
            infor.setInformativeText('Favor de insertar otro ID o ingresar uno')
            infor.setStandardButtons(QMessageBox.Ok)
            infor.setDefaultButton(QMessageBox.Ok)
            resu = infor.exec_()
            self.ui.idB.setText('')
            return False
        #Termina la conexión con la BD
        self.c.closeDBConnection(self.conn)
    def eliminar_mascota(self):
        #Asigna el valor del ID en la variable a
        a= self.ui.idB.text()
        #self.hide()
        #Si la línea de texto del ID no está vacía
        if a!='':
            #Muestra una ventana de confirmación
            confirm = QMessageBox.question(self, 'Mensaje', "¿Estas seguro que quieres borrar a la mascota encontrada?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            #Si la respuesta es sí
            if confirm == QMessageBox.Yes:
                
                #Eliminación del cliente en la BD
                eliminar = "DELETE from mascota WHERE idMascota = %s"
                self.cursor.execute(eliminar, (a))
                self.conn.commit()
                #Ventana que muestra que la operación fue exitosa
                infor = QMessageBox()
                infor.setIcon(QMessageBox.Information)
                infor.setWindowTitle('Información')
                infor.setText('Operación exitosa')
                infor.setInformativeText('Pulse Ok para continuar')
                infor.setStandardButtons(QMessageBox.Ok)
                infor.setDefaultButton(QMessageBox.Ok)
                resu = infor.exec_()
                #Los datos en las líneas de texto se borran
                self.ui.idB.setText('')
                self.ui.idB.setText('')
                self.ui.nomMascotaE.setText('')
                self.ui.nomDueE.setText('')
                self.ui.telefonoE.setText('')
                self.ui.correoE.setText('')
              
                #Desbloquea la inserción del ID, pero la bloquea en las demás líneas
                self.ui.idB.setReadOnly(False)
              
        #Si la línea de texto del ID está vacía
        else:
            #Ventana que muestra que no hay ningún ID insertado
            infor = QMessageBox()
            infor.setIcon(QMessageBox.Warning)
            infor.setWindowTitle('Advertencia')
            infor.setText('No hay ID insertado')
            infor.setInformativeText('Favor de insertar uno')
            infor.setStandardButtons(QMessageBox.Ok)
            infor.setDefaultButton(QMessageBox.Ok)
            resu = infor.exec_()
            #Borra los datos en las líneas de texto
            self.ui.idB.setText('')
            
            #Bloquea la inserción de datos en todas las líneas, exceptuando la del ID
            self.ui.idB.setReadOnly(False)

    def Salir(self):
        confirm = QMessageBox.question(self, 'Mensaje', "¿Quieres salir de la ventana?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if confirm == QMessageBox.Yes:
            self.hide()
  

if __name__ == '__main__':
    app = QApplication([])
    main = borrarMascota()
    main.show()
    sys.exit(app.exec())
    