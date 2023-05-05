'''
Calse: Eliminar Personal
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
from DeletePersonal import Ui_VentanaEliminarPersonal
from ConexionBD1 import Conexion


class ventanaEliminar(QMainWindow):
    def __init__(self):
        #Llamando a la interfáz
        super(ventanaEliminar, self).__init__()
        self.ui = Ui_VentanaEliminarPersonal()
        self.ui.setupUi(self)

        #Establece la conexion con la base de datos 
        self.c = Conexion()
        self.conne=self.c.CreateDBConnection("localhost",3306, "root", 'Luna-Pc', 'veterinaria', "root", "")
        self.cursor=self.conne.cursor()

        # Botones para difigirse a las funciones
        self.ui.pushButton_buscar.clicked.connect(self.buscar_personal)
        self.ui.pushButton_eliminar.clicked.connect(self.eliminar)
        self.ui.pushButton_volver.clicked.connect(self.salir)


        self.ui.lineNomPersonal.setText('')
        self.ui.lineCargoPersonal.setText('')
        self.ui.lineCorreoPersonal.setText('')
        self.ui.lineTelefonoPersonal.setText('')
    
    def buscar_personal(self, ide):
        busqueda = self.ui.lineID.text()
        resultado = self.consultar(busqueda)
        if resultado==True:
            
            #Selecciona sus atributos y los muestra en las líneas de texto
            query = "SELECT idPersonal, cargo, nombre, correo, telefono from personal WHERE idPersonal = '%s'" %busqueda
            self.cursor.execute(query)
            row = self.cursor.fetchone()
            if row != None:
                v = int(busqueda)
                if row[0]==v:
                    nombre = str (row[2])
        
                    cargo = str (row[1])

                    correo = str (row[3])
                
                    telefono = str (row[4])

                    self.ui.lineNomPersonal.setText(nombre )
                    self.ui.lineCargoPersonal.setText(cargo)
                    self.ui.lineCorreoPersonal.setText(correo)
                    self.ui.lineTelefonoPersonal.setText(telefono)


    def consultar(self, ide):
        #Consulta a la base de datos que busca el ID insertado (ide)
        query = "SELECT idPersonal FROM personal WHERE idPersonal = '%s'" % ide
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
            infor.setText('No existe algún personal con este ID o no hay ningun dato ingresado')
            infor.setInformativeText('Favor de insertar otro ID o ingresar uno')
            infor.setStandardButtons(QMessageBox.Ok)
            infor.setDefaultButton(QMessageBox.Ok)
            resu = infor.exec_()
            self.ui.lineID.setText('')
            return False
        #Termina la conexión con la BD
        

    

        

    def eliminar(self):
        #Asigna el valor del ID en la variable a
        id = self.ui.lineID.text()
        #self.hide()
        #Si la línea de texto del ID no está vacía
        if id!='':
            #Muestra una ventana de confirmación
            confirm = QMessageBox.question(self, 'Mensaje', "¿Estas seguro que quieres borrar a esta personal del personal?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            #Si la respuesta es sí
            if confirm == QMessageBox.Yes:
                
                #Eliminación del cliente en la BD
                eliminar = "DELETE from personal WHERE idPersonal = %s"
                self.cursor.execute(eliminar, (id))
                self.conne.commit()
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
                self.ui.lineID.setText('')
                self.ui.lineNomPersonal.setText('')
                self.ui.lineCargoPersonal.setText('')
                self.ui.lineCorreoPersonal.setText('')
                self.ui.lineTelefonoPersonal.setText('')
                #Desbloquea la inserción del ID, pero la bloquea en las demás líneas
                self.ui.lineID.setReadOnly(False)
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
            self.ui.lineID.setText('')
            
            #Bloquea la inserción de datos en todas las líneas, exceptuando la del ID
            self.ui.lineID.setReadOnly(False)



    #Funcion volver al menú       
    def salir(self):
        confirm = QMessageBox.question(self, 'Mensaje', "¿Estás seguro de querer volver al menú?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if confirm == QMessageBox.Yes:
            self.hide()
            self.c.closeDBConnection(self.conne)

if __name__ == '__main__':
    app = QApplication([])
    main = ventanaEliminar()
    main.show()
    sys.exit(app.exec())