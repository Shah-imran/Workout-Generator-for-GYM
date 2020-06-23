# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_to_workout.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import var
from pyautogui import alert


class Ui_Dialog(object):
    def __init__(self, name):
        self.name = name
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(200, 182)
        self.formLayout = QtWidgets.QFormLayout(Dialog)
        self.formLayout.setObjectName("formLayout")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setObjectName("comboBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.comboBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(2, QtWidgets.QFormLayout.SpanningRole, spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.SpanningRole, spacerItem1)
        self.pushButton_add = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_add.sizePolicy().hasHeightForWidth())
        self.pushButton_add.setSizePolicy(sizePolicy)
        self.pushButton_add.setObjectName("pushButton_add")
        self.pushButton_add.setStyleSheet(var.button_style)
        self.pushButton_add.setIcon(QtGui.QIcon(var.add_icon))
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.pushButton_add)
        self.pushButton_cancel = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_cancel.sizePolicy().hasHeightForWidth())
        self.pushButton_cancel.setSizePolicy(sizePolicy)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.pushButton_cancel.setStyleSheet(var.button_style)
        self.pushButton_cancel.setIcon(QtGui.QIcon(var.cancel_icon))
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.pushButton_cancel)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton_add.clicked.connect(self.add_to_workout)
        self.pushButton_cancel.clicked.connect(Dialog.close)
        self.Dialog = Dialog

        self.comboBox.addItems(["Set {}".format(i) for i in range(1,var.set_count+1)])
        try:
            index = self.comboBox.findText(var.last_sel, QtCore.Qt.MatchFixedString)
            if index >= 0:
                self.comboBox.setCurrentIndex(index)
        except:
            pass

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Add to Workout"))
        self.pushButton_add.setText(_translate("Dialog", "Add"))
        self.pushButton_cancel.setText(_translate("Dialog", "Cancel"))

    def add_to_workout(self):
        try:
            v_set = self.comboBox.currentText()
            temp = [self.name, "Reps", 0,15, 3, v_set]
            if len(var.workout_table) == 0 and len(var.workout_table) == 1:
                var.workout_table.append(temp)
            else:
                sets = [var.workout_table[i][5] for i in range(len(var.workout_table))]
                try:
                    index = len(sets) - sets[::-1].index(v_set)
                except:
                    index = -1

                if index == -1:
                    var.workout_table.append(temp)
                else:
                    var.workout_table.insert(index,temp)
            var.last_sel = v_set
            sets = [var.workout_table[i][5] for i in range(len(var.workout_table))]
            sets = list(set(sets))
            if len(sets)>1:
                for index, item in enumerate(var.workout_table):
                    if item[5] == temp[5] and item[1] != "AMRAP":
                        var.workout_table[index][4] = temp[4]
                if len(sets)==2:
                    key = var.workout_table[0][5]
                    for index, item in enumerate(var.workout_table):
                        if key == item[5] and item[1] != "AMRAP":
                            var.workout_table[index][4] = var.workout_table[0][4]
        except Exception as e:
            print("Error at {}".format(e))
        self.Dialog.close()

def main(name):
    dialog = QtWidgets.QDialog()
    dialog.ui = Ui_Dialog(name)
    dialog.ui.setupUi(dialog)
    return dialog.exec_()