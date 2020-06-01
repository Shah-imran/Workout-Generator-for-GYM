# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_exercise.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets, Qt
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
    def __init__(self, name):
        self.image_path = ""
        self.name = name
        self.exercise_info = ""
        self.calories = 0
        self.exercise_time = 0
        self.visible_for_user = 0
        self.exercise_id = list()
        self.muscle_group_id = list()
        self.muscle_name = list()
        try:
            conn = DB()
            exercise_id, exercise_info, muscle_group_id, muscle_name, calories, exercise_time, image_path, visible_for_user = conn.fetch_exercise_info3(name)
            conn.close()
            if image_path:
                self.image_path = image_path
            self.calories = calories
            self.exercise_id = exercise_id
            self.exercise_time = exercise_time
            self.exercise_info = exercise_info
            self.visible_for_user = visible_for_user
            self.muscle_group_id = muscle_group_id
            self.muscle_name = muscle_name
            print(exercise_id, exercise_info, muscle_group_id, muscle_name, calories, exercise_time, image_path, visible_for_user)
        except Exception as e:
            print("Error while fetching data from database - {}".format(e))

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
        self.lineEdit_name.setText(self.name)

        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.textEdit_info = QtWidgets.QTextEdit(Dialog)
        self.textEdit_info.setObjectName("textEdit_info")
        self.verticalLayout.addWidget(self.textEdit_info)
        self.textEdit_info.setText(self.exercise_info)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)

        self.comboBox_muscle_group = CheckableComboBox()
        self.comboBox_muscle_group.setObjectName("comboBox_muscle_group")

        for index in range(len(var.muscle_groups)):
            self.comboBox_muscle_group.addItem(var.muscle_groups[index])
            item = self.comboBox_muscle_group.model().item(index, 0)
            if var.muscle_groups[index] in self.muscle_name:
                item.setCheckState(QtCore.Qt.Checked)
            else:
                item.setCheckState(QtCore.Qt.Unchecked)

        self.verticalLayout.addWidget(self.comboBox_muscle_group)

        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.lineEdit_calories = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_calories.setObjectName("lineEdit_calories")
        self.verticalLayout.addWidget(self.lineEdit_calories)
        self.lineEdit_calories.setText(str(self.calories))
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.lineEdit_time = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_time.setObjectName("lineEdit_time")
        self.verticalLayout.addWidget(self.lineEdit_time)
        self.lineEdit_time.setText(str(self.exercise_time))
        self.checkBox_visible_for_users = QtWidgets.QCheckBox(Dialog)
        if self.visible_for_user == 1:
            self.checkBox_visible_for_users.setChecked(True)
        else:
            self.checkBox_visible_for_users.setChecked(False)
        self.checkBox_visible_for_users.setObjectName("checkBox_visible_for_users")
        self.verticalLayout.addWidget(self.checkBox_visible_for_users)
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setStyleSheet("background-color: #F0F0F0;")
        self.graphicsView.setFixedSize(445, 350)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        self.pushButton_add_image = QtWidgets.QPushButton(Dialog)
        self.pushButton_add_image.setObjectName("pushButton_add_image")
        self.pushButton_add_image.setStyleSheet(var.button_style)
        self.verticalLayout.addWidget(self.pushButton_add_image)
        self.pushButton_add_image.setIcon(QtGui.QIcon(var.add_icon))
        self.pushButton_update = QtWidgets.QPushButton(Dialog)
        self.pushButton_update.setObjectName("pushButton_save")
        self.pushButton_update.setStyleSheet(var.button_style)
        self.verticalLayout.addWidget(self.pushButton_update)
        self.pushButton_update.setIcon(QtGui.QIcon(var.edit_icon))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton_update.clicked.connect(self.push_to_db)
        self.pushButton_add_image.clicked.connect(self.image_picker)
        self.Dialog = Dialog

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Add exercise"))
        self.label.setText(_translate("Dialog", "Name:"))
        self.label_3.setText(_translate("Dialog", "Info:"))
        self.label_2.setText(_translate("Dialog", "Muscle group:"))
        self.label_4.setText(_translate("Dialog", "Calories:"))
        # self.lineEdit_calories.setText(_translate("Dialog", "2"))
        self.label_5.setText(_translate("Dialog", "Time in sec"))
        # self.lineEdit_time.setText(_translate("Dialog", "2"))
        self.checkBox_visible_for_users.setText(_translate("Dialog", "Visible for users"))
        self.pushButton_add_image.setText(_translate("Dialog", "Add Image"))
        self.pushButton_update.setText(_translate("Dialog", "Update"))

        self.show_image()

    def show_image(self):
        try:
            scene = Qt.QGraphicsScene()
            pix = Qt.QPixmap(self.image_path).scaled(445, 400, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
            scene.addPixmap(pix)
            self.graphicsView.setScene(scene)
            self.graphicsView.show()
        except:
            pass

    def image_picker(self):
        options = QFileDialog.Options()
        self.image_path = ""
        self.image_path, _ = QFileDialog.getOpenFileName(None,"Select a image","","image files (*.jpeg *.jpg *.png )", options=options)
        self.show_image()

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
                    muscle_id.append(conn.fetch_muscle_id(item.text()))
            print(muscle_id)

            if len(muscle_id) == len(self.muscle_group_id):
                for e_id, m_id in zip(self.exercise_id, muscle_id):
                    result = conn.update_exercise([name, info, m_id, calories, time, self.image_path, visible_for_user], e_id)
                    print([name, info, m_id, calories, time, self.image_path, visible_for_user], e_id)
            elif len(muscle_id) > len(self.muscle_group_id):
                for count in range(0, len(self.muscle_group_id)):
                    result = conn.update_exercise([name, info, muscle_id[count], calories, time, self.image_path, visible_for_user], self.exercise_id[count])
                    print("update")
                    print([name, info, muscle_id[count], calories, time, self.image_path, visible_for_user], self.exercise_id[count])
                for count in range(len(self.muscle_group_id), len(muscle_id)):
                    result = conn.add_exercise([name, info, muscle_id[count], calories, time, self.image_path], visible_for_user)
                    print("new")
                    print([name, info, muscle_id[count], calories, time, self.image_path], visible_for_user)
            else:
                for count in range(0, len(muscle_id)):
                    result = conn.update_exercise([name, info, muscle_id[count], calories, time, self.image_path, visible_for_user], self.exercise_id[count])
                for count in range(len(muscle_id), len(self.muscle_group_id)):
                    result = conn.remove_exercise_by_id(self.exercise_id[count])

            if result == True:
                alert(text='Success', title='Alert', button='OK')
            else:
                alert(text='Error - {}'.format(result), title='Alert', button='OK')
        except Exception as e:
            print("error at add_exercise push_to_db - {}".format(e))
            conn.close()

        finally:
            conn.close()
            self.Dialog.close()

def main(name):
    dialog = QtWidgets.QDialog()
    dialog.ui = Ui_Dialog(name)
    dialog.ui.setupUi(dialog)
    return dialog.exec_()
