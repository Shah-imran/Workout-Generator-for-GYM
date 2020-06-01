# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'save_workout.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import db
from pyautogui import alert
import var


class Ui_Dialog(object):
    def __init__(self, name):
        self.name = name

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(443, 244)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        Dialog.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.textEdit_info = QtWidgets.QTextEdit(Dialog)
        self.textEdit_info.setObjectName("textEdit_info")
        self.verticalLayout.addWidget(self.textEdit_info)
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.pushButton_ok = QtWidgets.QPushButton(Dialog)
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.pushButton_ok.setStyleSheet(var.button_style)
        self.verticalLayout.addWidget(self.pushButton_ok)
        self.pushButton_ok.setIcon(QtGui.QIcon(var.add_icon))
        self.pushButton_cancel = QtWidgets.QPushButton(Dialog)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.pushButton_cancel.setStyleSheet(var.button_style)
        self.verticalLayout.addWidget(self.pushButton_cancel)
        self.pushButton_cancel.setIcon(QtGui.QIcon(var.cancel_icon))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.dialog = Dialog

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Workout - {}".format(self.name)))
        self.label.setText(_translate("Dialog", "Info"))
        self.pushButton_ok.setText(_translate("Dialog", "Ok"))
        self.pushButton_cancel.setText(_translate("Dialog", "Cancel"))
        self.checkBox.setText(_translate("Dialog", "Visible for users"))
        self.pushButton_ok.clicked.connect(self.push_to_db)
        self.pushButton_cancel.clicked.connect(self.cancel)

    def push_to_db(self):
        try:
            conn = db.DB()
            exercise_id = list()

            result = conn.fetch_workout_name()

            if self.name not in result:
                for item in var.workout_table:
                    exercise_id.append(conn.fetch_exercise_id(item[0]))

                visible_for_user = 1
                if not self.checkBox.isChecked():
                    visible_for_user = 0

                info = self.textEdit_info.toPlainText()

                for item, id in zip(var.workout_table, exercise_id):
                    # if item[1] == "time":
                    print("Data - ")
                    print([self.name, info, id, int(item[5].split(" ")[1]), item[1], item[2], item[3], item[4]], visible_for_user)
                    result = conn.add_workout([self.name, info, id, int(item[5].split(" ")[1]), item[1], item[2], item[3], item[4]], visible_for_user)
                    print(result)
                    # else:
                    #     result = conn.add_workout([self.name, info, id, int(item[5].split(" ")[1]), item[1], 0, item[2], item[3]], visible_for_user)
                # w_name, info, exercise_id, set_count, type, time, reps, rounds, visible_for_user
                alert(text='Successfully Saved', title='Alert', button='OK')
            else:
                raise Exception("Already Exists")
        except Exception as e:
            alert(text='Error while saving - {}'.format(e), title='Alert', button='OK')
        finally:
            conn.close()
            self.dialog.close()


    def cancel(self):
        self.dialog.close()

def main(name):
    dialog = QtWidgets.QDialog()
    dialog.ui = Ui_Dialog(name)
    dialog.ui.setupUi(dialog)
    return dialog.exec_()
