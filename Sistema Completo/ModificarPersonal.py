'''
Clase: Modificar Personal
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
from UpdatePersonal import Ui_VentanaModificarPersonal
from ConexionBD1 import Conexion


class ventanaModificar(QMainWindow):
    def __init__(self):
        #Llamando a la interfáz
        super(ventanaModificar, self).__init__()
        self.ui = Ui_VentanaModificarPersonal()
        self.ui.setupUi(self)

        #Establece la conexion con la base de datos 
        self.c = Conexion()
        self.conne=self.c.CreateDBConnection("localhost",3306, "root", 'Luna-Pc', 'veterinaria', "root", "")
        self.cursor=self.conne.cursor()

        # Botones para difigirse a las funciones
        self.ui.pushButton_buscar.clicked.connect(self.update_producto)
        self.ui.pushButton_modificar.clicked.connect(self.Guardar)
        self.ui.pushButton_volver.clicked.connect(self.salir)


        self.ui.lineNomPersonal.setText('')
        self.ui.lineCargoPersonal.setText('')
        self.ui.lineCorreoPersonal.setText('')
        self.ui.lineTelefonoPersonal.setText('')
    
    def update_producto(self, ide):
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
        

    def Guardar(self):

        idPersonal=self.ui.lineID.text()
        nom = self.ui.lineNomPersonal.text()
        carg =  self.ui.lineCargoPersonal.text()
        corr = self.ui.lineCorreoPersonal.text()
        tel = self.ui.lineTelefonoPersonal.text()

        #Si todos los datos están llenos
        if idPersonal!='':
            #Actualiza los datos en la BD
            actualizar= "UPDATE personal SET nombre = %s WHERE idPersonal = %s"
            val = (nom, idPersonal)
            self.cursor.execute(actualizar,val)
            self.conne.commit()
            actualizar= "UPDATE personal SET cargo = %s WHERE idPersonal = %s"
            val = (carg, idPersonal)
            self.cursor.execute(actualizar, val)
            self.conne.commit()
            actualizar= "UPDATE personal SET correo = %s WHERE idPersonal = %s"
            val = (corr, idPersonal)
            self.cursor.execute(actualizar, val)
            self.conne.commit()
            actualizar= "UPDATE personal SET telefono = %s WHERE idPersonal = %s"
            val = (tel, idPersonal)
            self.cursor.execute(actualizar, val)
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
            #Borra los datos de las líneas de texto
            self.ui.lineID.setText('')
            self.ui.lineNomPersonal.setText('' )
            self.ui.lineCargoPersonal.setText('')
            self.ui.lineCorreoPersonal.setText('')
            self.ui.lineTelefonoPersonal.setText('')

            
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
            self.ui.lineNomPersonal.setText('' )
            self.ui.lineCargoPersonal.setText('')
            self.ui.lineCorreoPersonal.setText('')
            self.ui.lineTelefonoPersonal.setText('')


    #Funcion volver al menú       
    def salir(self):
        confirm = QMessageBox.question(self, 'Mensaje', "¿Estás seguro de querer volver al menú?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if confirm == QMessageBox.Yes:
            self.hide()
            self.c.closeDBConnection(self.conne)

if __name__ == '__main__':
    app = QApplication([])
    main = ventanaModificar()
    main.show()
    sys.exit(app.exec())