# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'consultarMascotas.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_consultarMascota(object):
    def setupUi(self, consultarMascota):
        consultarMascota.setObjectName("consultarMascota")
        consultarMascota.resize(582, 471)
        consultarMascota.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(consultarMascota)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 10, 111, 111))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("consultar.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 130, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.conMascota = QtWidgets.QTableWidget(self.centralwidget)
        self.conMascota.setGeometry(QtCore.QRect(30, 180, 511, 192))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.conMascota.setFont(font)
        self.conMascota.setObjectName("conMascota")
        self.conMascota.setColumnCount(5)
        self.conMascota.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.conMascota.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.conMascota.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.conMascota.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.conMascota.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.conMascota.setHorizontalHeaderItem(4, item)
        self.volver = QtWidgets.QPushButton(self.centralwidget)
        self.volver.setGeometry(QtCore.QRect(30, 390, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.volver.setFont(font)
        self.volver.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 255);")
        self.volver.setObjectName("volver")
        consultarMascota.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(consultarMascota)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 582, 21))
        self.menubar.setObjectName("menubar")
        consultarMascota.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(consultarMascota)
        self.statusbar.setObjectName("statusbar")
        consultarMascota.setStatusBar(self.statusbar)

        self.retranslateUi(consultarMascota)
        QtCore.QMetaObject.connectSlotsByName(consultarMascota)

    def retranslateUi(self, consultarMascota):
        _translate = QtCore.QCoreApplication.translate
        consultarMascota.setWindowTitle(_translate("consultarMascota", "MainWindow"))
        self.label_2.setText(_translate("consultarMascota", "Consultar Mascotas"))
        item = self.conMascota.horizontalHeaderItem(0)
        item.setText(_translate("consultarMascota", "ID Mascota"))
        item = self.conMascota.horizontalHeaderItem(1)
        item.setText(_translate("consultarMascota", "Mascota"))
        item = self.conMascota.horizontalHeaderItem(2)
        item.setText(_translate("consultarMascota", "Dueño"))
        item = self.conMascota.horizontalHeaderItem(3)
        item.setText(_translate("consultarMascota", "Teléfono"))
        item = self.conMascota.horizontalHeaderItem(4)
        item.setText(_translate("consultarMascota", "Correo"))
        self.volver.setText(_translate("consultarMascota", "Volver"))
