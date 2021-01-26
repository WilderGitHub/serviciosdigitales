# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'workmate01.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

  
  
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(354, 194)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 90, 131, 51))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 40, 47, 13))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 354, 21))
        self.menubar.setObjectName("menubar")
        self.menuAutomatizacion = QtWidgets.QMenu(self.menubar)
        self.menuAutomatizacion.setObjectName("menuAutomatizacion")
        self.menuComercio_de_Bienes = QtWidgets.QMenu(self.menuAutomatizacion)
        self.menuComercio_de_Bienes.setObjectName("menuComercio_de_Bienes")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExportaciones = QtWidgets.QAction(MainWindow)
        self.actionExportaciones.setObjectName("actionExportaciones")
        self.menuComercio_de_Bienes.addAction(self.actionExportaciones)
        self.menuAutomatizacion.addAction(self.menuComercio_de_Bienes.menuAction())
        self.menubar.addAction(self.menuAutomatizacion.menuAction())

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.label.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "WorkMate"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.menuAutomatizacion.setTitle(_translate("MainWindow", "Automatizacion"))
        self.menuComercio_de_Bienes.setTitle(_translate("MainWindow", "Comercio de Bienes"))
        self.actionExportaciones.setText(_translate("MainWindow", "Exportaciones"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
