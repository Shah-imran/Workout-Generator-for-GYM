# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_muscle.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from threading import Thread
from db import DB
from pyautogui import alert
import var

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(369, 156)
        self.formLayout = QtWidgets.QFormLayout(Dialog)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.checkBox_visible_for_user = QtWidgets.QCheckBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.checkBox_visible_for_user.setFont(font)
        self.checkBox_visible_for_user.setObjectName("checkBox_visible_for_user")
        self.checkBox_visible_for_user.setChecked(True)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.checkBox_visible_for_user)
        self.lineEdit_name = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.lineEdit_name)
        self.pushButton_add = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_add.sizePolicy().hasHeightForWidth())
        self.pushButton_add.setSizePolicy(sizePolicy)
        self.pushButton_add.setObjectName("pushButton_add")
        self.pushButton_add.setStyleSheet(var.button_style)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.pushButton_add)
        self.pushButton_add.setIcon(QtGui.QIcon(var.add_icon))
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton_add.clicked.connect(self.add_muscle_to_db)
        self.Dialog = Dialog
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Add Muscle Group"))
        self.label.setText(_translate("Dialog", "Name:"))
        self.checkBox_visible_for_user.setText(_translate("Dialog", "Visible for User"))
        self.pushButton_add.setText(_translate("Dialog", "Add"))

    def add_muscle_to_db(self):
        name = self.lineEdit_name.text().strip()
        visible_for_user = 1
        if not self.checkBox_visible_for_user.isChecked():
            visible_for_user = 0
        conn = DB()
        result = conn.add_muscle_group(name, visible_for_user)
        conn.close()
        if result == True:
            alert(text='Added to Database', title='Alert', button='OK')
        else:
            alert(text='Error - {}'.format(result), title='Alert', button='OK')
        self.Dialog.close()

def main():
    dialog = QtWidgets.QDialog()
    dialog.ui = Ui_Dialog()
    dialog.ui.setupUi(dialog)
    return dialog.exec_()
