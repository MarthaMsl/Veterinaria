#Clase: Consultar Cita
#Autor: Samuel Martinez Arenas
#Matricula: 181803022
#Fecha creación: 10/11/2022
#Última fecha de modificación: 27/10/2022
#Docente: Rebeca Rodríguez Huesca
#Materia: Ingeniería de requisitos
#Proyecto: Veterinaria

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit
from PyQt5 import QtWidgets, QtCore, QtGui

from consultarCita import Ui_consultarCita
from conexionCitas import ConexionBD



class ventanaConsultarCita(QMainWindow):
    def __init__(self):
        super(ventanaConsultarCita, self).__init__()
        self.ui = Ui_consultarCita()
        self.ui.setupUi(self)

        # Botones para difigirse a las funciones
        self.ui.volver.clicked.connect(self.salir)
        self.ui.consultar.clicked.connect(self.consulta_cita) 

        #Establece la conexion con la base de datos
        self.c = ConexionBD()
        self.conn=self.c.CreateDBConnection("localhost", 3306, "root", 'Familia Martuin', 'veterinaria', "root", "")
        self.cursor = self.conn.cursor()


        #Propiedades de la tabla - sirve para acomodar los datos
        self.ui.tableWidget.setColumnWidth(1,100)
        self.ui.tableWidget.setColumnWidth(2,98)
        self.ui.tableWidget.setColumnWidth(3,98)
        self.ui.tableWidget.setColumnWidth(4,98)
        self.ui.tableWidget.setColumnWidth(5,98)
        
        self.ui.calendarWidget.selectionChanged.connect(self.cambiar_fecha)


    # Funcion que obtiene la fecha ingresada en el calendario
    def cambiar_fecha(self):
        self.ui.fecha.setDate(self.ui.calendarWidget.selectedDate())
    
    #Funcion que cierra la ventana mostrada
    def salir(self):
        confirm = QMessageBox.question(self, 'Mensaje', "¿Quieres salir de la ventana?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if confirm == QMessageBox.Yes:
            self.hide()

    def consulta_cita(self):
        #Obtiene la fecha ingresado 
        fecha2 = self.cambiarFecha(self.ui.fecha.text())
        busqueda = fecha2 
        #Busca el id y lo guarda en una variable
        resultado = self.consultar(busqueda)
        self.ui.tableWidget.setRowCount(resultado)
        tablerow = 0
        # Si se encuentra el id
        if resultado==True:

            #hace un query seleccionando los datos requeridos de cierto id

            query = "SELECT personal.nombre, mascota.nombreMascota, fecha, hora, asuntoCita from personal, mascota, cita WHERE personal.idPersonal = cita.idPersonal and mascota.idMascota = cita.idMascota and cita.fecha = '%s'" %busqueda 
            self.cursor.execute(query)
            
            row = self.cursor.fetchone()
            print(row)
            if row != None:
                #Se hizo un casteo de las columnas para que los datos quedaran en orden respecto a la tabla

                fecha = row[0]
                FECHA = str(fecha)

                hora = row[1]
                HORA = str(hora)

                asuntocita = row[2]
                ASUNTOCITA = str(asuntocita)

                e = row[3]
                E = str(e)

                f = row[4]
                F = str(f)

                #Se posicionan los datos en la tabla    
                self.ui.tableWidget.setItem(tablerow,0,QtWidgets.QTableWidgetItem(FECHA))
                self.ui.tableWidget.setItem(tablerow,1,QtWidgets.QTableWidgetItem(HORA)) 
                self.ui.tableWidget.setItem(tablerow,2,QtWidgets.QTableWidgetItem(ASUNTOCITA))
                self.ui.tableWidget.setItem(tablerow,3,QtWidgets.QTableWidgetItem(E))	
                self.ui.tableWidget.setItem(tablerow,4,QtWidgets.QTableWidgetItem(F))
                tablerow +=1

                        
        #Si no hay citas en esa fecha
        else:
            #Muestra una ventana indicando que no existe esa fecha
            infor = QMessageBox()
            infor.setIcon(QMessageBox.Warning)
            infor.setWindowTitle('Advertencia')
            infor.setText('No hay fechas registradas para ese dia')
            infor.setInformativeText('Favor de insertar otra fecha')
            infor.setStandardButtons(QMessageBox.Ok)
            infor.setDefaultButton(QMessageBox.Ok)
            resu = infor.exec_()
            
    def consultar(self, ide):
        #Consulta a la base de datos que busca el ID insertado (ide)
        query = "SELECT idCita FROM cita WHERE fecha = '%s'" % ide
        self.cursor.execute(query)
        row = self.cursor.fetchone()
        print(row)
        #Buscando la fecha
        if row != None:
            return True
        else:
            return False
        #Termina la conexión con la BD
        self.c.closeDBConnection(self.conn)

    
    def consultarPersonal(self, ide):
        #Consulta a la base de datos que busca el ID insertado (ide)
        print(ide)
        query = "SELECT idPersonal FROM cita WHERE fecha = '%s'" % ide
        self.cursor.execute(query)
        row = self.cursor.fetchone()
        print(row)
        #Buscando la fecha
        if row != None:
            return row
        else:
            return False
        #Termina la conexión con la BD
        self.c.closeDBConnection(self.conn)

    
    def consultarMascota(self, ide):
        #Consulta a la base de datos que busca el ID insertado (ide)
        
        query = "SELECT idMascota FROM mascota WHERE fecha = '%s'" % ide
        self.cursor.execute(query)
        row = self.cursor.fetchone()
        print(row)
        #Buscando la fecha
        if row != None:
            return row
        else:
            return False
        #Termina la conexión con la BD
        self.c.closeDBConnection(self.conn)

    # Funcion que cambia el orden de la fecha para poder registrarse    
    def cambiarFecha(self, fecha):
        partes_fecha = fecha.split('/')

        return '{}{}{}'.format(partes_fecha[2],partes_fecha[1],partes_fecha[0])


if __name__ == '__main__':
    app = QApplication([])
    main = ventanaConsultarCita()
    main.show()
    sys.exit(app.exec())