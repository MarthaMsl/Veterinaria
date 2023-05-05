#Clase: Registrar Cita
#Autor: Samuel Martinez Arenas
#Matricula: 181803022
#Fecha creación: 10/11/2022
#Última fecha de modificación: 27/10/2022
#Docente: Rebeca Rodríguez Huesca
#Materia: Ingeniería de requisitos
#Proyecto: Veterinaria

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit, QTableWidgetItem, QDialog
from PyQt5 import  QtWidgets, QtCore, QtGui

from registrarCita import Ui_registrarCita 
from conexionCitas import ConexionBD


class ventanaCitas(QMainWindow):
    def __init__(self):
        super(ventanaCitas, self).__init__()
        self.ui = Ui_registrarCita()
        self.ui.setupUi(self)
        # Botones para difigirse a las funciones
        self.ui.registrar.clicked.connect(self.insert_citas)
        self.ui.volver.clicked.connect(self.salir)

        #Establece la conexion con la base de datos 
        self.c = ConexionBD()
        self.conn=self.c.CreateDBConnection("localhost", 3306, "root", 'Familia Martuin', 'veterinaria', "root", "")
        self.cursor = self.conn.cursor()
        self.CargarPersonal()
        self.CargarMascota()
        self.ui.calendarWidget.selectionChanged.connect(self.cambiar_fecha)


    # Funcion que obtiene la fecha ingresada en el calendario
    def cambiar_fecha(self):
        self.ui.dateFecha.setDate(self.ui.calendarWidget.selectedDate())

    # Funcion que hace posible mostrar el nombre de los personales en un combobox
    def CargarPersonal(self):
        combo = self.ui.idPersonal
        sql = "SELECT idPersonal, nombre FROM personal"
        self.cursor.execute(sql)
        model = self.cursor.fetchone()
        while model:
            self.ui.idPersonal.addItem(model[1])
            print(model[1])
            model = self.cursor.fetchone()

    # Funcion que hace posible mostrar el nombre de los clientes en un combobox
    def CargarMascota(self):
        combo = self.ui.idMascota
        sql = "SELECT idMascota, nombreMascota FROM mascota"
        self.cursor.execute(sql)
        model = self.cursor.fetchone()
        while model:
            combo.addItem(model[1])
            model = self.cursor.fetchone()
        
    #Funcion que obtiene el ID de la tabla Personal cuando se selecciona el nombre
    def ObtenerIdCombo(self):
        combo = self.ui.idPersonal
        row = combo.currentIndex()
        idx = combo.model().index(row, 0)   
        idcombo = combo.model().data(idx)
        return idcombo

    #Funcion que obtiene el ID de la tabla Clientes cuando se selecciona el nombre
    def ObtenerIdComboM(self):
        combo = self.ui.idMascota
        row = combo.currentIndex()
        idx = combo.model().index(row, 0)
        idcombo = combo.model().data(idx)
        return idcombo  
    

    #Funcion para poder registrar citas en la base de datos
    def insert_citas(self):
        nomMascota = self.ObtenerIdComboM()
        nomPersonal = self.ObtenerIdCombo()
        fecha = self.cambiarFecha(self.ui.dateFecha.text())
        hora = self.ui.hora.text()
        asuntoCita = self.ui.asunto.text()

        sqlfecha = "SELECT fecha, hora FROM cita"
        self.cursor.execute(sqlfecha)
        comprobacion = self.cursor.fetchall()
        # if fecha == comprobacion(row[0]):

        # hace un query seleccionando el id del nombre ingresado en los combobox
        sqlp = "Select idPersonal from personal WHERE nombre = '%s'" %nomPersonal
        self.cursor.execute(sqlp)
        idPersonal = self.cursor.fetchone()

        # hace un query seleccionando el id del nombre ingresado en los combobox
        sqlc = "Select idMascota from mascota WHERE nombreMascota = '%s'" %nomMascota
        self.cursor.execute(sqlc)
        idMascota = self.cursor.fetchone()      
        
        # Si todos los datos estan llenos
        if (idPersonal!='') and (idMascota!='') and (fecha!='') and (hora!='') and (asuntoCita!=''):
            sql="INSERT INTO cita (idPersonal ,idMascota, fecha, hora, asuntoCita) values(%s,%s,%s,%s,%s)"
            self.cursor.execute(sql,(idPersonal, idMascota, fecha, hora, asuntoCita))
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
            self.ui.hora.clear()

            self.ui.hora.setText('')
            self.ui.asunto.setText('')
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

    # Funcion que cambia el orden de la fecha para poder registrarse    
    def cambiarFecha(self, fecha):
        partes_fecha = fecha.split('/')

        return '{}{}{}'.format(partes_fecha[2]+'/',partes_fecha[1]+'/',partes_fecha[0])
         
    #Funcion que cierra la ventana mostrada        
    def salir(self):
        confirm = QMessageBox.question(self, 'Mensaje', "¿Quieres salir de la ventana?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if confirm == QMessageBox.Yes:
            self.hide()

if __name__ == '__main__':
    app = QApplication([])
    main = ventanaCitas()
    main.show()
    sys.exit(app.exec())