
#ESte error lo corriges con este truco si es que molesta mucho https://www.youtube.com/watch?v=6T7hDqB8LA8
from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from appStreaming02 import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(355, 180)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 100, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.BotonEscogerArchivo = QtWidgets.QPushButton(self.centralwidget)
        self.BotonEscogerArchivo.setGeometry(QtCore.QRect(50, 30, 121, 23))
        self.BotonEscogerArchivo.setObjectName("BotonEscogerArchivo")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 355, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        print("MATI")
        self.BotonEscogerArchivo.clicked.connect(self.EscogerArchivoOe)
        self.pushButton.clicked.connect(self.procesarOe)
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Procesar"))
        self.BotonEscogerArchivo.setText(_translate("MainWindow", "Escoger Archivo"))
        global rutas
        rutas =[]
        global ruta
        ruta=''
    def EscogerArchivoOe(self):
        archivin = QtWidgets.QFileDialog.getOpenFileName()
        ruta = archivin[0]
        rutas.append(ruta)
    def procesarOe(self):
        miFuncion(rutas)    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    