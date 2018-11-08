# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hbc.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(400, 400)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setStyleSheet("")
        MainWindow.setProperty("WindowStaysOnTopHint", True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.heroComboBox = ExtendedComboBox(self.centralwidget)
        self.heroComboBox.setGeometry(QtCore.QRect(0, 0, 201, 25))
        self.heroComboBox.setAccessibleName("")
        self.heroComboBox.setEditable(True)
        self.heroComboBox.setObjectName("heroComboBox")
        self.heroComboBox.addItem("")
        self.heroComboBox.setStyleSheet("QComboBox { color: white; background-color: rgba(0, 0, 0, 0.7); font-size: 15px; }")
        self.talentComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.talentComboBox.setGeometry(QtCore.QRect(0, 30, 201, 25))
        self.talentComboBox.setMinimumContentsLength(0)
        self.talentComboBox.setObjectName("talentComboBox")
        self.talentComboBox.addItem("")
        self.talentComboBox.setStyleSheet("QComboBox { color: white; background-color: rgba(0, 0, 0, 0.7); font-size: 15px; }")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 70, 201, 181))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.setWordWrap(True)
        self.label.setStyleSheet("QLabel { color: white; qproperty-alignment: AlignCenter; background-color: rgba(0, 0, 0, 0.7); font-size: 15px; font-weight: bold; }")
        MainWindow.setCentralWidget(self.centralwidget)

        # Careful, should replace this here every time this file changes
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Heroes Builds Cheatsheet"))
        self.heroComboBox.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.heroComboBox.setItemText(0, _translate("MainWindow", "Choose hero"))
        self.talentComboBox.setItemText(0, _translate("MainWindow", "Choose build"))

from extendedComboBox import ExtendedComboBox
