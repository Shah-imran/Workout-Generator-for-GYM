# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_exercise.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from pyautogui import alert
import var
from db import DB

class CheckableComboBox(QtWidgets.QComboBox):
    def __init__(self):
        super(CheckableComboBox, self).__init__()
        self.view().pressed.connect(self.handleItemPressed)
        self.setModel(QtGui.QStandardItemModel(self))

    def handleItemPressed(self, index):
        item = self.model().itemFromIndex(index)
        if item.checkState() == QtCore.Qt.Checked:
            item.setCheckState(QtCore.Qt.Unchecked)
        else:
            item.setCheckState(QtCore.Qt.Checked)

class Ui_Dialog(object):
    def __init__(self):
        self.image_path = ""
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(389, 553)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        Dialog.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit_name = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.verticalLayout.addWidget(self.lineEdit_name)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.textEdit_info = QtWidgets.QTextEdit(Dialog)
        self.textEdit_info.setObjectName("textEdit_info")
        self.verticalLayout.addWidget(self.textEdit_info)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)

        self.comboBox_muscle_group = CheckableComboBox()
        self.comboBox_muscle_group.setObjectName("comboBox_muscle_group")

        for index in range(len(var.muscle_groups)):
            self.comboBox_muscle_group.addItem(var.muscle_groups[index])
            item = self.comboBox_muscle_group.model().item(index, 0)
            item.setCheckState(QtCore.Qt.Unchecked)

        self.verticalLayout.addWidget(self.comboBox_muscle_group)

        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.lineEdit_calories = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_calories.setObjectName("lineEdit_calories")
        self.verticalLayout.addWidget(self.lineEdit_calories)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.lineEdit_time = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_time.setObjectName("lineEdit_time")
        self.verticalLayout.addWidget(self.lineEdit_time)
        self.checkBox_visible_for_users = QtWidgets.QCheckBox(Dialog)
        self.checkBox_visible_for_users.setChecked(True)
        self.checkBox_visible_for_users.setObjectName("checkBox_visible_for_users")
        self.verticalLayout.addWidget(self.checkBox_visible_for_users)
        self.pushButton_add_image = QtWidgets.QPushButton(Dialog)
        self.pushButton_add_image.setObjectName("pushButton_add_image")
        self.pushButton_add_image.setStyleSheet(var.button_style)
        self.verticalLayout.addWidget(self.pushButton_add_image)
        self.pushButton_add_image.setIcon(QtGui.QIcon(var.add_icon))
        self.pushButton_save = QtWidgets.QPushButton(Dialog)
        self.pushButton_save.setObjectName("pushButton_save")
        self.pushButton_save.setStyleSheet(var.button_style)
        self.verticalLayout.addWidget(self.pushButton_save)
        self.pushButton_save.setIcon(QtGui.QIcon(var.save_icon))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton_save.clicked.connect(self.push_to_db)
        self.pushButton_add_image.clicked.connect(self.image_picker)
        self.Dialog = Dialog
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Add exercise"))
        self.label.setText(_translate("Dialog", "Name:"))
        self.label_3.setText(_translate("Dialog", "Info:"))
        self.label_2.setText(_translate("Dialog", "Muscle group:"))
        self.label_4.setText(_translate("Dialog", "Calories:"))
        self.lineEdit_calories.setText(_translate("Dialog", "2"))
        self.label_5.setText(_translate("Dialog", "Time in sec"))
        self.lineEdit_time.setText(_translate("Dialog", "2"))
        self.checkBox_visible_for_users.setText(_translate("Dialog", "Visible for users"))
        self.pushButton_add_image.setText(_translate("Dialog", "Add Image"))
        self.pushButton_save.setText(_translate("Dialog", "Save"))

    def image_picker(self):
        options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog
        self.image_path = ""
        self.image_path, _ = QFileDialog.getOpenFileName(None,"Select a image","","image files (*.jpeg *.jpg *.png )", options=options)

    def push_to_db(self):
        try:
            conn = DB()
            name = self.lineEdit_name.text()
            info = self.textEdit_info.toPlainText()
            visible_for_user = 1
            if not self.checkBox_visible_for_users.isChecked():
                visible_for_user = 0
            calories =  int(self.lineEdit_calories.text())
            time = int(self.lineEdit_time.text())
            muscle_id = list()
            for index in range(len(var.muscle_groups)):
                item = self.comboBox_muscle_group.model().item(index, 0)
                if item.checkState() == QtCore.Qt.Checked:
                    result = conn.fetch_exercise(var.muscle_groups[index])
                    if name not in result:
                        muscle_id.append(conn.fetch_muscle_id(var.muscle_groups[index]))

            print("Muscle_id len - {}".format(len(muscle_id)))
            for item in muscle_id:
                result = conn.add_exercise([name, info, item, calories, time, self.image_path], visible_for_user)
            if result == True:
                alert(text='Success', title='Alert', button='OK')
            else:
                alert(text='Failed', title='Alert', button='OK')
            conn.close()
        except Exception as e:
            print("error at add_exercise push_to_db - {}".format(e))
            conn.close()

        finally:
            self.Dialog.close()

def main():
    dialog = QtWidgets.QDialog()
    dialog.ui = Ui_Dialog()
    dialog.ui.setupUi(dialog)
    return dialog.exec_()
