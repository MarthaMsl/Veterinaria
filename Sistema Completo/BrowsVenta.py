# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VentanaConsultarVentas.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VentanaConsultarVentas(object):
    def setupUi(self, VentanaConsultarVentas):
        VentanaConsultarVentas.setObjectName("VentanaConsultarVentas")
        VentanaConsultarVentas.setWindowModality(QtCore.Qt.NonModal)
        VentanaConsultarVentas.resize(592, 651)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(VentanaConsultarVentas.sizePolicy().hasHeightForWidth())
        VentanaConsultarVentas.setSizePolicy(sizePolicy)
        VentanaConsultarVentas.setMinimumSize(QtCore.QSize(592, 651))
        VentanaConsultarVentas.setAutoFillBackground(False)
        VentanaConsultarVentas.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ConsultarVentasWindow = QtWidgets.QWidget(VentanaConsultarVentas)
        self.ConsultarVentasWindow.setObjectName("ConsultarVentasWindow")
        self.label = QtWidgets.QLabel(self.ConsultarVentasWindow)
        self.label.setGeometry(QtCore.QRect(240, 10, 141, 131))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Buscar.jpeg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.ConsultarVentasWindow)
        self.label_2.setGeometry(QtCore.QRect(240, 150, 151, 31))
        self.label_2.setStyleSheet("font: 87 12pt \"Arial Black\";")
        self.label_2.setObjectName("label_2")
        self.pushButton_volver_2 = QtWidgets.QPushButton(self.ConsultarVentasWindow)
        self.pushButton_volver_2.setGeometry(QtCore.QRect(160, 590, 75, 23))
        self.pushButton_volver_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"Arial\";\n"
"background-color: rgb(0, 0, 255) ;")
        self.pushButton_volver_2.setObjectName("pushButton_volver_2")
        self.Calendario = QtWidgets.QCalendarWidget(self.ConsultarVentasWindow)
        self.Calendario.setGeometry(QtCore.QRect(30, 230, 311, 171))
        self.Calendario.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.Calendario.setObjectName("Calendario")
        self.tableVenta = QtWidgets.QTableWidget(self.ConsultarVentasWindow)
        self.tableVenta.setGeometry(QtCore.QRect(350, 191, 211, 211))
        self.tableVenta.setObjectName("tableVenta")
        self.tableVenta.setColumnCount(2)
        self.tableVenta.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        item.setFont(font)
        self.tableVenta.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        item.setFont(font)
        self.tableVenta.setHorizontalHeaderItem(1, item)
        self.label_3 = QtWidgets.QLabel(self.ConsultarVentasWindow)
        self.label_3.setGeometry(QtCore.QRect(70, 440, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font: 12pt \"Arial\";")
        self.label_3.setObjectName("label_3")
        self.TablaDetalle = QtWidgets.QTableWidget(self.ConsultarVentasWindow)
        self.TablaDetalle.setGeometry(QtCore.QRect(350, 420, 211, 192))
        self.TablaDetalle.setObjectName("TablaDetalle")
        self.TablaDetalle.setColumnCount(2)
        self.TablaDetalle.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        item.setFont(font)
        self.TablaDetalle.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        item.setFont(font)
        self.TablaDetalle.setHorizontalHeaderItem(1, item)
        self.label_4 = QtWidgets.QLabel(self.ConsultarVentasWindow)
        self.label_4.setGeometry(QtCore.QRect(70, 480, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.IdeV = QtWidgets.QLineEdit(self.ConsultarVentasWindow)
        self.IdeV.setGeometry(QtCore.QRect(160, 480, 71, 31))
        self.IdeV.setStyleSheet("font: 12pt \"Arial\";")
        self.IdeV.setObjectName("IdeV")
        self.BtBuscarIde = QtWidgets.QPushButton(self.ConsultarVentasWindow)
        self.BtBuscarIde.setGeometry(QtCore.QRect(240, 480, 61, 31))
        self.BtBuscarIde.setStyleSheet("color: rgb(rgb(0, 0, 0));\n"
"font: 12pt \"Arial\";\n"
"background-color: rgb(255, 170, 0) ;")
        self.BtBuscarIde.setObjectName("BtBuscarIde")
        self.label_5 = QtWidgets.QLabel(self.ConsultarVentasWindow)
        self.label_5.setGeometry(QtCore.QRect(70, 530, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.labelTotal = QtWidgets.QLabel(self.ConsultarVentasWindow)
        self.labelTotal.setGeometry(QtCore.QRect(160, 530, 141, 31))
        self.labelTotal.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelTotal.setStyleSheet("font: 75 16pt \"Arial\";\n"
"background-color:rgb(0, 170, 255);")
        self.labelTotal.setObjectName("labelTotal")
        self.dateConsultar = QtWidgets.QDateEdit(self.ConsultarVentasWindow)
        self.dateConsultar.setGeometry(QtCore.QRect(90, 190, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.dateConsultar.setFont(font)
        self.dateConsultar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"")
        self.dateConsultar.setObjectName("dateConsultar")
        self.BtBuscarDate = QtWidgets.QPushButton(self.ConsultarVentasWindow)
        self.BtBuscarDate.setGeometry(QtCore.QRect(210, 190, 61, 31))
        self.BtBuscarDate.setStyleSheet("color: rgb(rgb(0, 0, 0));\n"
"font: 12pt \"Arial\";\n"
"background-color: rgb(255, 170, 0) ;")
        self.BtBuscarDate.setObjectName("BtBuscarDate")
        VentanaConsultarVentas.setCentralWidget(self.ConsultarVentasWindow)
        self.menubar = QtWidgets.QMenuBar(VentanaConsultarVentas)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 592, 21))
        self.menubar.setObjectName("menubar")
        VentanaConsultarVentas.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(VentanaConsultarVentas)
        self.statusbar.setObjectName("statusbar")
        VentanaConsultarVentas.setStatusBar(self.statusbar)

        self.retranslateUi(VentanaConsultarVentas)
        QtCore.QMetaObject.connectSlotsByName(VentanaConsultarVentas)

    def retranslateUi(self, VentanaConsultarVentas):
        _translate = QtCore.QCoreApplication.translate
        VentanaConsultarVentas.setWindowTitle(_translate("VentanaConsultarVentas", "VentanaConsultarVenta"))
        self.label_2.setText(_translate("VentanaConsultarVentas", "Consultar Ventas"))
        self.pushButton_volver_2.setText(_translate("VentanaConsultarVentas", "Volver"))
        item = self.tableVenta.horizontalHeaderItem(0)
        item.setText(_translate("VentanaConsultarVentas", "ID Ventas"))
        item = self.tableVenta.horizontalHeaderItem(1)
        item.setText(_translate("VentanaConsultarVentas", "Total Venta"))
        self.label_3.setText(_translate("VentanaConsultarVentas", "Para consultar el detalle de venta:"))
        item = self.TablaDetalle.horizontalHeaderItem(0)
        item.setText(_translate("VentanaConsultarVentas", "Producto"))
        item = self.TablaDetalle.horizontalHeaderItem(1)
        item.setText(_translate("VentanaConsultarVentas", "Cantidad"))
        self.label_4.setText(_translate("VentanaConsultarVentas", "Teclea el ID:"))
        self.BtBuscarIde.setText(_translate("VentanaConsultarVentas", "Buscar"))
        self.label_5.setText(_translate("VentanaConsultarVentas", "Total:"))
        self.labelTotal.setText(_translate("VentanaConsultarVentas", "$"))
        self.BtBuscarDate.setText(_translate("VentanaConsultarVentas", "Buscar"))
