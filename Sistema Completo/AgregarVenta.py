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
from MoreVenta import Ui_VentanaMoreVenta


class OtraVenta(QMainWindow):
    def __init__(self):
        #Llamando a la interfáz
        super(OtraVenta, self).__init__()
        self.ui = Ui_VentanaMoreVenta()
        self.ui.setupUi(self)

        #Establece la conexion con la base de datos 
        self.c = Conexion()
        self.conne=self.c.CreateDBConnection("localhost",3306, "root", 'Luna-Pc', 'veterinaria', "root", "")
        self.cursor=self.conne.cursor()

        self.ui.pushButton_registrar.clicked.connect(self.ingresar)
        self.ui.pushButton_volver.clicked.connect(self.salir)
        self.ui.pushButton_MasProducto.clicked.connect(self.agregar)
        
        self.CargarProducto()

        #intanciando las variables para lograr la fecha y hora de la venta
        hora = datetime.now()
        minutos = datetime.now()
        segundos = datetime.now()
        dia = datetime.now()
        mes = datetime.now()
        anio = datetime.now()
        #Corroborando que sean correctas las instancias
        print (hora.hour,':',minutos.minute)
        print(dia.day,'/',mes.month,'/',anio.year)
        #Concatenación de variables
        h = str(hora.hour)+':'+str(minutos.minute)+':'+str(segundos.second)
        f = str(anio.year)+'-'+str(mes.month)+'-'+str(dia.day)
        #insertando las cadenas concatenadas en los linedit
        self.ui.LineFecha.setText(f)
        self.ui.LineHora.setText(h)
        #Propiedades de la tabla - sirve para acomodar los datos
        self.ui.tableVenta.setColumnWidth(0,100)
        self.ui.tableVenta.setColumnWidth(1,55)
        self.ui.tableVenta.setColumnWidth(2,72)
        self.ui.tableVenta.setColumnWidth(3,50)

        
    #Función para llenar el combobox
    def CargarProducto(self):
        combo = self.ui.comboBoxProducto
        sql = "SELECT idProducto, nombreProducto FROM producto"
        self.cursor.execute(sql)
        model = self.cursor.fetchone()
        
        while model:
            combo.addItem(model[1])
            print(model[1])
            model = self.cursor.fetchone()
            

    #Función para mostrar la venta en la tabla
    def agregar(self):
        a = self.ui.LineHora.text()
        b = self.ui.LineFecha.text()
        c= str(self.ui.comboBoxProducto.currentText())
        print('linea 87',c)
        d= self.ui.spinBoxCantidad.value()
        
        if(d==0):
            #Muestra una ventana de advertencia cuando faltan líneas de texto por llenar
                info = QMessageBox()
                info.setIcon(QMessageBox.Warning)
                info.setWindowTitle('Advertencia')
                info.setText('Faltan datos por llenar')
                info.setInformativeText('Favor de llenar todos los datos')
                info.setStandardButtons(QMessageBox.Ok)
                info.setDefaultButton(QMessageBox.Ok)
                result = info.exec_()
        else:
            #Si todos los atributos están llenos
            d= str(d)
            if (b!='') and (a!='') and (c!='') and (d!=0):
                cons= "SELECT producto.nombreProducto, producto.precio from producto WHERE nombreProducto = '%s'" %c
                self.cursor.execute(cons)
            
                row= self.cursor.fetchone()
                print('linea97 ',row)
                if row != None:
                #Se hizo un casteo de las columnas para que los datos quedaran en orden respecto a la tabla
                        
                    nombreProducto = row[0]
                    PRODUCTO = str(nombreProducto)
                    precio = row[1]
                    PRECIO = str(precio)
                    cantidad = str(d)
                    subtotal = float(precio)
                    sub = float(cantidad)
                    subtotal *= sub
                    subtotal = str(subtotal)
                    
                    #Se posicionan los datos en la tabla
                
                    
                    var = self.ui.tableVenta.rowCount()
                    
                    #Bloquea la modificación de atributos

                    
                    self.ui.LineFecha.setReadOnly(True)
                    self.ui.LineHora.setReadOnly(True)
                    index= self.ui.comboBoxProducto.currentIndex()
                    self.ui.comboBoxProducto.removeItem(index)
                    
                    #Cuenta las filas de la tabla
                    row= self.ui.tableVenta.rowCount()
                    #Inserta los datos en la tabla
                    self.ui.tableVenta.insertRow(row)
                    self.ui.tableVenta.setItem(row, 0, QtWidgets.QTableWidgetItem(PRODUCTO))
                    self.ui.tableVenta.setItem(row, 1, QtWidgets.QTableWidgetItem(PRECIO))
                    self.ui.tableVenta.setItem(row, 2, QtWidgets.QTableWidgetItem(cantidad))
                    self.ui.tableVenta.setItem(row, 3, QtWidgets.QTableWidgetItem(subtotal))
                    self.obtenerCosto()
                    self.ActualizarInventario(PRODUCTO,cantidad)
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
                
            #Si al menos una de las líneas de texto está vacía
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
                self.ui.LineHora.setText()
                self.ui.LineFecha.setText()
                self.ui.comboBoxProducto.setCurrentText()


    #Funcion para calcular el costo de la venta
    def obtenerCosto(self):
        conteo= self.ui.tableVenta.rowCount()
        co=0
        co= float(co)
        for i in range(0, conteo):
            count= self.ui.tableVenta.item(i, 3).text()
            cont= float(count)
            co+=cont
        co= str(co)
        self.ui.labelTotal.setText(co)
    #Funcion para Actualizar Inventario
    def ActualizarInventario(self,prod,cant):

        sql = "SELECT idProducto, nombreProducto FROM producto WHERE nombreProducto = '%s' "  %prod
        self.cursor.execute(sql)
        row = self.cursor.fetchone()
        #Función para actualizar el inventario
        if row!=None:
            prod = str(row[0])
        #Creando la variable @x 
        producto = "SELECT cantidadProducto into @x FROM producto WHERE idProducto = '%s'" %prod
        self.cursor.execute(producto)
        self.conne.commit()
        #Línea para hacer el decremento en inventario
        asignar = "set @x = @x - '%s'" %cant
        self.cursor.execute(asignar)
        self.conne.commit() 
        #Actualizando los datos en inventario
        producto = "update producto set cantidadProducto = @x where idProducto = '%s'" %prod
        self.cursor.execute(producto)
        self.conne.commit()
        print("si funciona")

    def DetalleVenta(self,p,c,price):
        h = self.ui.LineHora.text()
        query3="SELECT idVenta FROM ventas where hora = '%s'  "%h
        self.cursor.execute(query3)
        var2 = self.cursor.fetchone()
        print('linea228',var2)
        if var2!=None:
            res = str(var2[0])
            print('linea231 ->ID VENTA encontrado',res)
            query="SELECT idProducto FROM producto where nombreProducto = '%s'  "%p
            self.cursor.execute(query)
            ide = self.cursor.fetchone()
            print('linea261',ide)
            query1= "INSERT INTO detalle_ventas(idVenta, idProducto, cantidad, precio) values (%s, %s, %s, %s)"
            self.cursor.execute(query1, (res, ide, c, price ))
            self.conne.commit()
            print('linea 239',query1)
       
    

    #Funcion para guardar la venta en la base de datos    
    def ingresar(self):
        com=0
        #Cuenta la cantidad de filas en la tabla
        
        
        #Para cada elemento en cada una de las filas
        
        h = self.ui.LineHora.text()
        f = self.ui.LineFecha.text()
        t = self.ui.labelTotal.text()
        p = self.ui.comboBoxProducto.currentText()
        c = self.ui.spinBoxCantidad.value()
        #print('linea200->VariableProducto de la tabla',pro)
        #Si todos los atributos están llenos
        if (c==0):
            info = QMessageBox()
            info.setIcon(QMessageBox.Warning)
            info.setWindowTitle('Advertencia')
            info.setText('Faltan datos por llenar')
            info.setInformativeText('Favor de llenar todos los datos')
            info.setStandardButtons(QMessageBox.Ok)
            info.setDefaultButton(QMessageBox.Ok)
            result = info.exec_()
        else:
            #Query para insertar la venta en la base de datos
            insertar= "INSERT INTO ventas(fecha, hora, importeTotal) values ( %s, %s,%s)"
            self.cursor.execute(insertar, (f, h, t))
            self.conne.commit()
            
            #Query para consultar si existe la venta en la base de datos
            query3="SELECT idVenta FROM ventas where hora = '%s'  "%h
            self.cursor.execute(query3)
            var2 = self.cursor.fetchone()

            #Si existe ingresa los datos al detalle de la venta        
            if var2!=None:
                filas = self.ui.tableVenta.rowCount()
                for i in range (0,filas):
                    prod = self.ui.tableVenta.item(i,0).text()
                    
                    cant = self.ui.tableVenta.item(i,2).text()
                    
                    query3="SELECT idProducto, precio FROM producto WHERE nombreProducto = '%s'"%prod
                    self.cursor.execute(query3)
                    var3 = self.cursor.fetchone()
                    if var3!=None:
                        if var3[1]==prod:
                            prod = str(var3[0])
                        pro = str(var3[0])
                        precio = str(var3[1])

                    query4 = "INSERT INTO detalle_ventas (idVenta, idProducto, cantidad, precio) values (%s, %s, %s, %s)"
                    self.cursor.execute(query4, (var2, pro, cant, precio))
                    self.conne.commit()
                    print(query4)
                com=1
                #Si logró insertar los datos en una tupla
                if com==1:
                    infor = QMessageBox()
                    infor.setIcon(QMessageBox.Information)
                    infor.setWindowTitle('Información')
                    infor.setText('Operación exitosa')
                    infor.setInformativeText('Pulse Ok para continuar')
                    infor.setStandardButtons(QMessageBox.Ok)
                    infor.setDefaultButton(QMessageBox.Ok)
                    resu = infor.exec_()
                #Si no logró insertar los datos en una tupla
                #Manda a llamar el limpiado de la tabla   
                self.borrarTabla()
                
                self.ui.LineFecha.setReadOnly(False)
                self.ui.LineHora.setReadOnly(False)
                self.ui.spinBoxCantidad.setValue(1)
                self.ui.comboBoxProducto.clear()
                self.CargarProducto()
                self.ui.labelTotal.setText('0')
                self.c.closeDBConnection(self.conne)
        #Si la línea de texto con el ID está vacía

    #Funcion que consulta si la venta ya existe en la base de datos
    def consultar(self, ide):
        #Consulta a la base de datos que busca el ID insertado (ide)
        query = "SELECT idVenta FROM ventas WHERE idVenta = '%s'" % ide
        self.cursor.execute(query)
        row = self.cursor.fetchone()
        print(row)
        #Buscando el ID
        if row != None:
            #Se debe convertir el ID en entero, debido a que entró a la función como cadena de caracteres, para compararlo con los valores enteros de los ID en la BD.
            ide = int(ide)
            #Si encontró coincidencias devuelve True
            if row[0] == ide:
                self.c.closeDBConnection(self.conne)
                return True
            #De lo contrario, devuelve False
            else:
                self.c.closeDBConnection(self.conne)
                return False
        else:
            print("No hay compras con ese ID")
            self.c.closeDBConnection(self.conne)
            return False
        #Termina la conexión con la BD
        self.c.closeDBConnection(self.conne)
    
    #Funciión para borrar la tabla al finalizar una venta
    def borrarTabla(self):
        row= self.ui.tableVenta.rowCount()
        while row>-1:
            self.ui.tableVenta.removeRow(row)
            row-=1

    #Funcion volver al menú       
    def salir(self):
        confirm = QMessageBox.question(self, 'Mensaje', "¿Estás seguro de querer volver al menú?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if confirm == QMessageBox.Yes:
            self.hide()
    
if __name__ == '__main__':
    app = QApplication([])
    main = OtraVenta()
    main.show()
    
    
    sys.exit(app.exec())
