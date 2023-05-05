#Clase: Eiminar Cita
#Autor: Samuel Martinez Arenas
#Matricula: 181803022
#Fecha creación: 10/11/2022
#Última fecha de modificación: 27/10/2022
#Docente: Rebeca Rodríguez Huesca
#Materia: Ingeniería de requisitos
#Proyecto: Veterinaria

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit
from PyQt5 import uic, QtWidgets, QtCore, QtGui
from conexionCitas import ConexionBD
from eliminarCita import Ui_MainWindow

class ventanaEliminar(QMainWindow):
    def __init__(self):
        super(ventanaEliminar, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Botones para difigirse a las funciones
        self.ui.eliminar.clicked.connect(self.eliminar_cita)
        self.ui.buscar.clicked.connect(self.buscar)
        self.ui.volver.clicked.connect(self.salir)

        #Establece la conexion con la base de datos
        self.c = ConexionBD()
        self.conn=self.c.CreateDBConnection("localhost", 3306, "root", 'Familia Martuin', 'veterinaria', "root", "")
        self.cursor = self.conn.cursor()
        
    def buscar(self):
        #Obtiene el ID ingresado
        busqueda = self.ui.id.text()
        resultado = self.consultar(busqueda)
        
        # Si se encuentra el id
        if resultado==True:
            #Selecciona sus atributos y los muestra en la línea de texto
            query = "SELECT cita.idCita, personal.nombre, mascota.nombreMascota, fecha, hora, asuntoCita from personal, mascota, cita WHERE personal.idPersonal = cita.idPersonal and mascota.idMascota = cita.idMascota and cita.idCita = '%s'" %busqueda
            self.cursor.execute(query)
            row = self.cursor.fetchone()
            if row != None:
                v = int(busqueda)
                if row[0] == v:
                    np=str(row[1])
                    nm=str(row[2])
                    fe=str(row[3])
                    ho=str(row[4])
                    ac=str(row[5])
                
                #Se posicionan los datos en los line
                self.ui.personal.setText(np)
                self.ui.mascota.setText(nm)
                self.ui.fecha.setText(fe)
                self.ui.hora.setText(ho)
                self.ui.asunto.setText(ac)            
        
    def eliminar_cita(self):
        elim = self.ui.id.text()
        if elim != '':
            #Muestra una ventana de confirmación
            confirm = QMessageBox.question(self, 'Mensaje', "¿Quieres borrar al usuario encontrado?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            #Si la respuesta es sí
            if confirm == QMessageBox.Yes:
                #Eliminación del cliente en la BD
                eliminar = "DELETE from cita WHERE idCita = %s"
                self.cursor.execute(eliminar, (elim))
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
                self.ui.id.setText('')
                self.ui.personal.setText('')
                self.ui.mascota.setText('')
                self.ui.fecha.setText('')
                self.ui.hora.setText('')
                self.ui.asunto.setText('')
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
            self.ui.id.setText('')
            


    def consultar(self, ide):
        #Consulta a la base de datos que busca el ID insertado (ide)
        query = "SELECT idCita FROM cita WHERE idCita = '%s'" % ide
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
            #Muestra una ventana indicando que no existe ese ID
            infor = QMessageBox()
            infor.setIcon(QMessageBox.Warning)
            infor.setWindowTitle('Advertencia')
            infor.setText('No existe un cliente con ese ID o no hay ningun dato ingresado')
            infor.setInformativeText('Favor de insertar otro ID o ingresar uno')
            infor.setStandardButtons(QMessageBox.Ok)
            infor.setDefaultButton(QMessageBox.Ok)
            resu = infor.exec_()
            self.ui.id.setText('')
            return False
        #Termina la conexión con la BD
        self.c.closeDBConnection(self.conn)

    def consultarPersonal(self, ide):
        #Consulta a la base de datos que busca el ID insertado (ide)
        print(ide)
        query = "SELECT idPersonal FROM cita WHERE idCita = '%s'" % ide
        self.cursor.execute(query)
        row = self.cursor.fetchone()
        print(row)
        #Buscando el id
        if row != None:
            return row
        else:
            return False
        #Termina la conexión con la BD
        self.c.closeDBConnection(self.conn)
    
    def consultarCliente(self, ide):
        #Consulta a la base de datos que busca el ID insertado (ide)
        print(ide)
        query = "SELECT idMascota FROM mascota WHERE idMascota = '%s'" % ide
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

        
    #Funcion que cierra la ventana mostrada
    def salir(self):
        confirm = QMessageBox.question(self, 'Mensaje', "¿Quieres salir de la ventana?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if confirm == QMessageBox.Yes:
            self.hide()

if __name__ == '__main__':
    app = QApplication([])
    main = ventanaEliminar()
    main.show()
    sys.exit(app.exec())