'''
Clase: Agregar Venta
Autor: Martha Soto Luna
Matricula: 181803008
Fecha creación: 11/11/2022
Última fecha de modificación: 14/11/2022
Docente: Rebeca Rodríguez Huesca
Materia: Ingeniería de requisitos
Proyecto: Veterinaria
Versión: 2.0
'''

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit, QTableWidgetItem, QDialog
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from datetime import datetime
import importlib 


from ConexionBD1 import Conexion
from BrowsVenta import Ui_VentanaConsultarVentas


class ventanaConsultar(QMainWindow):
    def __init__(self):
        #Llamando a la interfáz
        super(ventanaConsultar, self).__init__()
        self.ui = Ui_VentanaConsultarVentas()
        self.ui.setupUi(self)

        #Establece la conexion con la base de datos 
        self.c = Conexion()
        self.conne=self.c.CreateDBConnection("localhost",3306, "root", 'Luna-Pc', 'veterinaria', "root", "")
        self.cursor=self.conne.cursor()

        # Botones para dirigirse a las funciones
        self.ui.BtBuscarDate.clicked.connect(self.ConsultarVentas)
        self.ui.BtBuscarIde.clicked.connect(self.ConsultarDetalleVentas)
        self.ui.pushButton_volver_2.clicked.connect(self.salir)

       


        self.ui.tableVenta.setColumnWidth(0,80)
        self.ui.tableVenta.setColumnWidth(1,90)
        self.ui.TablaDetalle.setColumnWidth(0,80)
        self.ui.TablaDetalle.setColumnWidth(1,95)

        self.ui.Calendario.selectionChanged.connect(self.cambiar_fecha)
    
    def cambiar_fecha(self):
        self.ui.dateConsultar.setDate(self.ui.Calendario.selectedDate())

    def cambiarFecha(self, fecha):
        partes_fecha = fecha.split('/')
        dia = datetime.now()
        mes = datetime.now()
        anio = datetime.now()
        #Corroborando que sean correctas las instancias
        d = int(dia.day)
        m = int(mes.month)
        y = int(anio.year)

        di = int(partes_fecha[0])
        me = int(partes_fecha[1])
        ye = int(partes_fecha[2])
        
        if(ye > y and me > m and di > d ):
            info = QMessageBox()
            info.setIcon(QMessageBox.Warning)
            info.setWindowTitle('Advertencia')
            info.setText('La fecha es mayor al día de hoy')
            info.setInformativeText('No existen ventas futuras')
            info.setStandardButtons(QMessageBox.Ok)
            info.setDefaultButton(QMessageBox.Ok)
            result = info.exec_()
        else:
            return '{}{}{}'.format(partes_fecha[2],partes_fecha[1],partes_fecha[0])

    #Función para consultar las ventas    
    def ConsultarVentas(self):
        busqueda =self.cambiarFecha(self.ui.dateConsultar.text())
        
        #Busca el id y lo guarda en una variable
        resultado = self.consultarVenta(busqueda)
        print(resultado)
        print(busqueda)
        tablerow = 0
        # Si se encuentra el id
        if resultado==True:
            query = "SELECT idVenta, importeTotal  FROM  ventas WHERE fecha = '%s'" %busqueda 
            self.cursor.execute(query)
            #print(query)
            raw = self.cursor.fetchall()
            i = len(raw)
            self.ui.tableVenta.setRowCount(i) 
            tablerow = 0
            #Ciclo para mostrar los datos en la tabla
            for row in raw:
                #Casteo de las variables
                idVenta = row[0]
                ID = str(idVenta)
                importeTotal = row[1]
                TOTAL = str(importeTotal)
                self.ui.tableVenta.setItem(tablerow,0,QtWidgets.QTableWidgetItem(ID))			
                self.ui.tableVenta.setItem(tablerow,1,QtWidgets.QTableWidgetItem(TOTAL))
                tablerow +=1
        else:
                info = QMessageBox()
                info.setIcon(QMessageBox.Warning)
                info.setWindowTitle('Advertencia')
                info.setText('No se encontraron ventas para esa fecha')
                info.setInformativeText('Intenta con otra diferente')
                info.setStandardButtons(QMessageBox.Ok)
                info.setDefaultButton(QMessageBox.Ok)
                result = info.exec_()
    #Función para consultar las ventas    
    def ConsultarDetalleVentas(self):
     
        ide = self.ui.IdeV.text()
        
       
        tablerow = 0
        # Si se encuentra el id
        if(ide!=''):
            query = "SELECT producto.nombreProducto, detalle_ventas.cantidad FROM producto, detalle_ventas where producto.idProducto = detalle_ventas.idProducto and detalle_ventas.idVenta = '%s'" %ide 
            self.cursor.execute(query)
            #print(query)
            raw = self.cursor.fetchall()
            i = len(raw)
            self.ui.TablaDetalle.setRowCount(i) 
            tablerow = 0
            #Ciclo para mostrar los datos en la tabla
            for row in raw:
                #Casteo de las variables
                nombreProducto = row[0]
                name = str(nombreProducto)
                cantidad = row[1]
                cant = str(cantidad)
                self.ui.TablaDetalle.setItem(tablerow,0,QtWidgets.QTableWidgetItem(name))			
                self.ui.TablaDetalle.setItem(tablerow,1,QtWidgets.QTableWidgetItem(cant))
                tablerow +=1
            query2 = "SELECT importeTotal from ventas WHERE idVenta = '%s'" %ide 
            self.cursor.execute(query2)
            tot = self.cursor.fetchone()
            t =str(tot[0])
            self.ui.labelTotal.setText(t)
        else:
                info = QMessageBox()
                info.setIcon(QMessageBox.Warning)
                info.setWindowTitle('Advertencia')
                info.setText('No has ingresado un ID')
                info.setInformativeText('Teclea uno para continuar')
                info.setStandardButtons(QMessageBox.Ok)
                info.setDefaultButton(QMessageBox.Ok)
                result = info.exec_()
    
    def consultarVenta(self, ide):
        #Consulta a la base de datos que busca el ID insertado (ide)
        query = "SELECT idVenta FROM ventas WHERE fecha = '%s'" % ide
        self.cursor.execute(query)
        row = self.cursor.fetchone()
        #Buscando la fecha
        if row != None:
            return True
        else:
            return False
        #generacion de pdf

    #Funcion volver al menú       
    def salir(self):
        self.hide()



if __name__ == '__main__':
    app = QApplication([])
    main = ventanaConsultar()
    main.show()
    
    sys.exit(app.exec())
