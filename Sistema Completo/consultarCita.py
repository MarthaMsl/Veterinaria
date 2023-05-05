# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'consultarCita.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_consultarCita(object):
    def setupUi(self, consultarCita):
        consultarCita.setObjectName("consultarCita")
        consultarCita.resize(901, 473)
        consultarCita.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(consultarCita)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(390, 10, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(430, 50, 111, 101))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("consultar.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 160, 51, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.fecha = QtWidgets.QDateEdit(self.centralwidget)
        self.fecha.setGeometry(QtCore.QRect(100, 160, 110, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.fecha.setFont(font)
        self.fecha.setObjectName("fecha")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(40, 190, 312, 183))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.calendarWidget.setFont(font)
        self.calendarWidget.setStyleSheet("background-color: rgb(0, 155, 232);")
        self.calendarWidget.setObjectName("calendarWidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(380, 190, 511, 181))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.volver = QtWidgets.QPushButton(self.centralwidget)
        self.volver.setGeometry(QtCore.QRect(160, 390, 91, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.volver.setFont(font)
        self.volver.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 255);")
        self.volver.setObjectName("volver")
        self.consultar = QtWidgets.QPushButton(self.centralwidget)
        self.consultar.setGeometry(QtCore.QRect(620, 390, 91, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.consultar.setFont(font)
        self.consultar.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 127, 0);")
        self.consultar.setObjectName("consultar")
        consultarCita.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(consultarCita)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 901, 21))
        self.menubar.setObjectName("menubar")
        consultarCita.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(consultarCita)
        self.statusbar.setObjectName("statusbar")
        consultarCita.setStatusBar(self.statusbar)

        self.retranslateUi(consultarCita)
        QtCore.QMetaObject.connectSlotsByName(consultarCita)

    def retranslateUi(self, consultarCita):
        _translate = QtCore.QCoreApplication.translate
        consultarCita.setWindowTitle(_translate("consultarCita", "MainWindow"))
        self.label.setText(_translate("consultarCita", "Consultar Citas"))
        self.label_3.setText(_translate("consultarCita", "Fecha:"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("consultarCita", "Personal"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("consultarCita", "Mascota"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("consultarCita", "Fecha"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("consultarCita", "Hora"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("consultarCita", "Asunto Cita"))
        self.volver.setText(_translate("consultarCita", "Volver"))
        self.consultar.setText(_translate("consultarCita", "Consultar"))
