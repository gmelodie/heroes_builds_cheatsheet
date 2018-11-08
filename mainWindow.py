# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hbc.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(202, 200)
        MainWindow.setStyleSheet("")
        MainWindow.setProperty("WindowStaysOnTopHint", True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.heroComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.heroComboBox.setGeometry(QtCore.QRect(0, 0, 201, 25))
        self.heroComboBox.setAccessibleName("")
        self.heroComboBox.setEditable(False)
        self.heroComboBox.setObjectName("heroComboBox")
        self.heroComboBox.addItem("")
        self.talentComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.talentComboBox.setGeometry(QtCore.QRect(0, 30, 201, 25))
        self.talentComboBox.setMinimumContentsLength(0)
        self.talentComboBox.setObjectName("talentComboBox")
        self.talentComboBox.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 70, 141, 141))
        self.label.setText("")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Heroes Builds Cheatsheet"))
        self.heroComboBox.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.heroComboBox.setItemText(0, _translate("MainWindow", "Choose hero"))
        self.talentComboBox.setItemText(0, _translate("MainWindow", "Choose build"))

