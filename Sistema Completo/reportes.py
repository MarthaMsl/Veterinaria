#Calse: reportes
#Autor: Samuel Martinez Arenas
#Matricula: 181803022
#Fecha creación: 25/10/2022
#Última fecha de modificación: 27/10/2022
#Docente: Rebeca Rodríguez Huesca
#Materia: Ingeniería de requisitos
#Proyecto: Veterinaria


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit
from PyQt5.QtGui import QIcon, QFont, QTextDocument
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter, QPrintPreviewDialog
from PyQt5.uic import loadUi
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QFileDialog


from generaReporte import Ui_generaReporte
from conexionReportes import ConexionBD
from fpdf import FPDF
#Establece la conexion con la base de datos
        
class ventanaGenera(QMainWindow):
    def __init__(self):
        
        super(ventanaGenera, self).__init__()
        self.ui = Ui_generaReporte()
        self.ui.setupUi(self)
        self.documento = QTextDocument()
        #self.c = Registro_datos()
        self.c = ConexionBD()
        self.conn=self.c.CreateDBConnection("localhost", 3306, "root", 'Familia Martiun', 'veterinaria', "root", "")
        self.cursor = self.conn.cursor()
        
        self.ui.pushButton_2.clicked.connect(self.Salir)
        self.ui.pushButton_3.clicked.connect(self.PDF)
        
        self.ui.pushButton.clicked.connect(self.consultarRepo)

        self.ui.tableWidget.setColumnWidth(0,98)
        self.ui.tableWidget.setColumnWidth(1,100)
        #self.ui.tableWidget.setColumnWidth(2,98)
        #self.ui.tableWidget.setColumnWidth(2,98)
        
        self.ui.calendarWidget.selectionChanged.connect(self.cambiar_fecha)
    
    def cambiar_fecha(self):
        self.ui.dateEdit.setDate(self.ui.calendarWidget.selectedDate())

    def cambiarFecha(self, fecha):
        partes_fecha = fecha.split('/')
        return '{}{}{}'.format(partes_fecha[2],partes_fecha[1],partes_fecha[0])

   

    def consultarRepo(self):
        print("entrando")

        #Obtiene la fecha ingresado 
        busqueda = self.cambiarFecha(self.ui.dateEdit.text())
        
        #Busca el id y lo guarda en una variable
        resultado = self.consultarVenta(busqueda)
        print(resultado)
        print(busqueda)
        
        tablerow = 0
        # Si se encuentra el id
        if resultado==True:
            self.obtenerCosto(busqueda)
            #hace un query seleccionando los datos requeridos de cierto id
            query = "SELECT hora, importeTotal  FROM  ventas WHERE fecha = '%s'" %busqueda 
            self.cursor.execute(query)
            #print(query)
            raw = self.cursor.fetchall()
            i=len(raw)
            self.ui.tableWidget.setRowCount(i)

            print(raw)

            for row in raw:
                #Se hizo un casteo de las columnas para que los datos quedaran en orden respecto a la tabla
                #fecha = row[0]
                #FECHA = str(fecha)

                hora = row[0]
                HORA = str(hora)

                #cant = row[2]
                #CANTIDAD = str(cant)

                total = row[1]
                TOTAL = str(total)
               

                #self.ui.tableWidget.setItem(tablerow,0,QtWidgets.QTableWidgetItem(FECHA))			
                self.ui.tableWidget.setItem(tablerow,0,QtWidgets.QTableWidgetItem(HORA))				
                #self.ui.tableWidget.setItem(tablerow,2,QtWidgets.QTableWidgetItem(CANTIDAD))
                self.ui.tableWidget.setItem(tablerow,1,QtWidgets.QTableWidgetItem(TOTAL))
                
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
            self.ui.dateEdit.setDate(self.ui.calendarWidget.selectedDate())
            #casteo de fecha dia mes y año

    #Funcion para sumar el total de la venta del día
    def obtenerCosto(self,busqueda):
        query = "SELECT importeTotal  FROM  ventas WHERE fecha = '%s'" %busqueda 
        self.cursor.execute(query)
        raw = self.cursor.fetchall()
        print('linea125',raw)
        lista=[]
        for row in raw:
                importeTotal = row[0]
                TOTAL = int(importeTotal)
                lista.append(TOTAL)
        c = sum(lista)
        c= str(c)
        self.ui.inCos.setText(c)


    #Función para verificar si existen ventas de ese día
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
    
    #Función para generar el pdf
    def PDF(self):
        try:
            if(self.ui.dateEdit.text()!=''):
                busqueda =self.cambiarFecha(self.ui.dateEdit.text())
                lista = []
                c=0
                #seleccion de atributos de la tabla en la bd
                quer = ("SELECT hora, importeTotal  FROM ventas WHERE fecha = %s")
                self.cursor.execute(quer, (busqueda))
                row = self.cursor.fetchone()
                while row:
                    c+=1
                    row = self.cursor.fetchone()
                for i in range(c):
                    lista.append(['']*2)
                    print(lista)
                    #invocacion de atributos de atributos de la tabla en la bd para el uso en la lista
                quer = ("SELECT hora, importeTotal  FROM ventas WHERE fecha = %s")
                self.cursor.execute(quer, (busqueda))
                row = self.cursor.fetchone()
                co=0
                while row:
                    a=row[0]
                    #b=row[1]
                    c=row[1]
                    #d=row[3]

                    print(type(a))
                    #print(type(b))
                    print(type(c))
                    #print(type(d))

                    lista[co][0]= str(a)
                    #lista[co][1]= str(b)
                    lista[co][1]= str(c)
                    #lista[co][3]= str(d)

                    co+=1
                    row = self.cursor.fetchone()
                print(lista)
                pdf= FPDF()
                pdf.set_font('Arial', size=12)
                pdf.add_page()     
                pdf.cell(w = 0, h = 0, txt = 'Reporte de ventas', border = 0, ln=0, align = 'C', fill = 0)
                pdf.ln(4)
                #pdf.cell(w = 45, h = 15, txt = 'Fecha', border = 1,align = 'C', fill = 0)
                pdf.cell(w = 45, h = 15, txt = 'Hora', border = 1,align = 'C', fill = 0)
                #pdf.cell(w = 45, h = 15, txt = 'Cantidad de Productos', border = 1,align = 'C', fill = 0)
                pdf.cell(w = 45, h = 15, txt = 'Importe Total', border = 1,align = 'C', fill = 0)
                pdf.ln()
               
                #creacionde la lista que manda el query
                for f in lista:
                    for item in f:
                        pdf.cell(w=45, h=10,txt=item, border=1, align='C')
                    pdf.ln(10)
                pdf.output('Reporte de Venta.pdf')
                print(lista)
                infor = QMessageBox()
                infor.setIcon(QMessageBox.Information)
                infor.setWindowTitle('Información')
                infor.setText('PDF creado con exito')
                infor.setInformativeText('Pulse Ok para continuar')
                infor.setStandardButtons(QMessageBox.Ok)
                infor.setDefaultButton(QMessageBox.Ok)
                resu = infor.exec_()

            else:
                raise Exception
        except Exception:
            info = QMessageBox()
            info.setIcon(QMessageBox.Warning)
            info.setWindowTitle('Advertencia')
            info.setText('Ha ocurrido un error')
            info.setInformativeText('Operación fallida, intentalo de nuevo')
            info.setStandardButtons(QMessageBox.Ok)
            info.setDefaultButton(QMessageBox.Ok)
            result = info.exec_()
            #resultado = self.consultarVenta(busqueda)
            #self.ui.lineEdit.setText('')
            busqueda = self.ui.dateEdit.text()
            self.ui.dateEdit.setReadOnly(False)
        finally:
            del lista[:]
    
    def Salir(self):
        confirm = QMessageBox.question(self, 'Mensaje', "¿Quieres salir de la ventana?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if confirm == QMessageBox.Yes:
            self.hide()
        
if __name__ == '__main__':
    app = QApplication([])
    main = ventanaGenera()
    main.show()
    sys.exit(app.exec())