# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menuprincipalSistema.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 627)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.menuprin = QtWidgets.QLabel(self.centralwidget)
        self.menuprin.setGeometry(QtCore.QRect(0, 0, 801, 611))
        self.menuprin.setText("")
        self.menuprin.setPixmap(QtGui.QPixmap("menuprincipal.jpg"))
        self.menuprin.setScaledContents(True)
        self.menuprin.setObjectName("menuprin")
        self.pushButton_Personal = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Personal.setGeometry(QtCore.QRect(120, 320, 101, 31))
        self.pushButton_Personal.setStyleSheet("\n"
"\n"
"QPushButton{\n"
"\n"
"    background-color: rgb(255, 255, 255) ;\n"
"    \n"
"    font: 63 11pt \"Bahnschrift SemiBold\";\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    background-color:  rgb(170, 255, 255);\n"
"    font: 63 11pt \"Bahnschrift SemiBold\";\n"
"    \n"
"}")
        self.pushButton_Personal.setObjectName("pushButton_Personal")
        self.pushButton_Citas = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Citas.setGeometry(QtCore.QRect(350, 320, 101, 31))
        self.pushButton_Citas.setStyleSheet("\n"
"\n"
"QPushButton{\n"
"\n"
"    background-color: rgb(255, 255, 255) ;\n"
"    \n"
"    font: 63 11pt \"Bahnschrift SemiBold\";\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    background-color:  rgb(170, 255, 255);\n"
"    font: 63 11pt \"Bahnschrift SemiBold\";\n"
"    \n"
"}")
        self.pushButton_Citas.setObjectName("pushButton_Citas")
        self.pushButton_Mascotas = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Mascotas.setGeometry(QtCore.QRect(600, 320, 101, 31))
        self.pushButton_Mascotas.setStyleSheet("\n"
"\n"
"QPushButton{\n"
"\n"
"    background-color: rgb(255, 255, 255) ;\n"
"    \n"
"    font: 63 11pt \"Bahnschrift SemiBold\";\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    background-color:  rgb(170, 255, 255);\n"
"    font: 63 11pt \"Bahnschrift SemiBold\";\n"
"    \n"
"}")
        self.pushButton_Mascotas.setObjectName("pushButton_Mascotas")
        self.pushButton_Ventas = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Ventas.setGeometry(QtCore.QRect(210, 540, 101, 31))
        self.pushButton_Ventas.setStyleSheet("\n"
"\n"
"QPushButton{\n"
"\n"
"    background-color: rgb(255, 255, 255) ;\n"
"    \n"
"    font: 63 11pt \"Bahnschrift SemiBold\";\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    background-color:  rgb(170, 255, 255);\n"
"    font: 63 11pt \"Bahnschrift SemiBold\";\n"
"    \n"
"}")
        self.pushButton_Ventas.setObjectName("pushButton_Ventas")
        self.pushButton_Productos = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Productos.setGeometry(QtCore.QRect(490, 540, 101, 31))
        self.pushButton_Productos.setStyleSheet("\n"
"\n"
"QPushButton{\n"
"\n"
"    background-color: rgb(255, 255, 255) ;\n"
"    \n"
"    font: 63 11pt \"Bahnschrift SemiBold\";\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    background-color:  rgb(170, 255, 255);\n"
"    font: 63 11pt \"Bahnschrift SemiBold\";\n"
"    \n"
"}")
        self.pushButton_Productos.setObjectName("pushButton_Productos")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_Personal.setText(_translate("MainWindow", "Personal"))
        self.pushButton_Citas.setText(_translate("MainWindow", "Citas"))
        self.pushButton_Mascotas.setText(_translate("MainWindow", "Mascotas"))
        self.pushButton_Ventas.setText(_translate("MainWindow", "Ventas"))
        self.pushButton_Productos.setText(_translate("MainWindow", "Productos"))
