from PyQt5 import QtCore, QtGui, QtWidgets
import var
from pyautogui import alert

class Ui_Dialog(object):

    def __init__(self, index):
        self.index = index
        self.set_init = ''
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(389, 322)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        Dialog.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 2, 1, 1)
        self.radioButton_reps = QtWidgets.QRadioButton(Dialog)
        self.radioButton_reps.setObjectName("radioButton_reps")
        self.gridLayout.addWidget(self.radioButton_reps, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 2, 1, 1)
        self.radioButton_amrap = QtWidgets.QRadioButton(Dialog)
        self.radioButton_amrap.setObjectName("radioButton_amrap")
        self.gridLayout.addWidget(self.radioButton_amrap, 1, 2, 1, 1)
        self.lineEdit_reps = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_reps.setObjectName("lineEdit_reps")
        self.gridLayout.addWidget(self.lineEdit_reps, 4, 1, 1, 1)
        self.lineEdit_time = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_time.setObjectName("lineEdit_time")
        self.gridLayout.addWidget(self.lineEdit_time, 6, 1, 1, 1)
        self.pushButton_remove = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_remove.sizePolicy().hasHeightForWidth())
        self.pushButton_remove.setSizePolicy(sizePolicy)
        self.pushButton_remove.setObjectName("pushButton_remove")
        self.gridLayout.addWidget(self.pushButton_remove, 8, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.lineEdit_rounds = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_rounds.setObjectName("lineEdit_rounds")
        self.gridLayout.addWidget(self.lineEdit_rounds, 6, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 5, 0, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)
        self.lineEdit_value = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_value.setObjectName("lineEdit_value")
        self.gridLayout.addWidget(self.lineEdit_value, 4, 0, 1, 1)
        self.lineEdit_time_amrap = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_time_amrap.setObjectName("lineEdit_time_amrap")
        self.gridLayout.addWidget(self.lineEdit_time_amrap, 6, 2, 1, 1)
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 1)
        self.lineEdit_reps_amrap = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_reps_amrap.setObjectName("lineEdit_reps_amrap")
        self.gridLayout.addWidget(self.lineEdit_reps_amrap, 4, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 1, 1, 1)
        self.radioButton_reps_in_time = QtWidgets.QRadioButton(Dialog)
        self.radioButton_reps_in_time.setObjectName("radioButton_reps_in_time")
        self.gridLayout.addWidget(self.radioButton_reps_in_time, 1, 1, 1, 1)
        self.radioButton_time = QtWidgets.QRadioButton(Dialog)
        self.radioButton_time.setChecked(True)
        self.radioButton_time.setObjectName("radioButton_time")
        self.gridLayout.addWidget(self.radioButton_time, 1, 0, 1, 1)
        self.pushButton_update = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_update.sizePolicy().hasHeightForWidth())
        self.pushButton_update.setSizePolicy(sizePolicy)
        self.pushButton_update.setObjectName("pushButton_update")
        self.gridLayout.addWidget(self.pushButton_update, 7, 1, 1, 1, QtCore.Qt.AlignHCenter)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.Dialog = Dialog

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.radioButton_reps_in_time.setText(_translate("Dialog", "EMOM"))
        self.label_3.setText(_translate("Dialog", "Reps(EMOM)"))
        self.lineEdit_reps.setText(_translate("Dialog", "15"))
        self.label_4.setText(_translate("Dialog", "Time(EMOM)"))
        self.lineEdit_time.setText(_translate("Dialog", "60"))
        Dialog.setWindowTitle(_translate('Dialog', 'Execise Name: {}'.format(var.workout_table[self.index][0])))
        self.label_2.setText(_translate('Dialog', 'Rounds'))
        self.radioButton_time.setText(_translate('Dialog', 'Time (is sec)'))
        self.lineEdit_rounds.setText(_translate('Dialog', '{}'.format(var.workout_table[self.index][4])))
        self.radioButton_reps.setText(_translate('Dialog', 'Reps'))
        self.label.setText(_translate('Dialog', 'Value'))
        self.label_6.setText(_translate("Dialog", "Total set time(in min)"))
        self.label_5.setText(_translate("Dialog", "Reps(AMRAP)"))
        self.radioButton_amrap.setText(_translate("Dialog", "AMRAP"))
        self.lineEdit_time_amrap.setText(_translate("Dialog", "0"))
        self.lineEdit_reps_amrap.setText(_translate("Dialog", "0"))
        self.pushButton_update.setStyleSheet(var.button_style)
        self.pushButton_remove.setStyleSheet(var.button_style)
        self.pushButton_update.setIcon(QtGui.QIcon(var.edit_icon))
        self.pushButton_remove.setIcon(QtGui.QIcon(var.delete_icon))
        # [self.name, "reps", 0, 15, 3, v_set]

        if var.workout_table[self.index][1] == 'Reps':
            self.radioButton_reps.setChecked(True)
            self.lineEdit_value.setText(_translate('Dialog', '{}'.format(var.workout_table[self.index][3])))
            self.lineEdit_time.setText("0")
            self.lineEdit_reps.setText("0")

        elif var.workout_table[self.index][1] == "EMOM":
            self.radioButton_reps_in_time.setChecked(True)
            self.lineEdit_value.setText(_translate('Dialog', '{}'.format(0)))
            self.lineEdit_time.setText(str(var.workout_table[self.index][2]))
            self.lineEdit_reps.setText(str(var.workout_table[self.index][3]))

        elif var.workout_table[self.index][1] == "AMRAP":
            self.radioButton_amrap.setChecked(True)
            self.lineEdit_value.setText("0")
            self.lineEdit_time.setText("0")
            self.lineEdit_rounds.setText("0")
            self.lineEdit_reps.setText("0")
            self.lineEdit_time_amrap.setText(str(var.workout_table[self.index][2]))
            self.lineEdit_reps_amrap.setText(str(var.workout_table[self.index][3]))

        else:
            self.radioButton_time.setChecked(True)
            self.lineEdit_value.setText(_translate('Dialog', '{}'.format(var.workout_table[self.index][2])))
            self.lineEdit_time.setText("0")
            self.lineEdit_reps.setText("0")

        self.comboBox.addItems(['Set {}'.format(i) for i in range(1, var.set_count + 1)])
        index = self.comboBox.findText(var.workout_table[self.index][5], QtCore.Qt.MatchFixedString)
        if index >= 0:
            self.comboBox.setCurrentIndex(index)

        self.pushButton_update.setText(_translate('Dialog', 'Update'))
        self.pushButton_remove.setText(_translate('Dialog', 'Remove'))
        self.pushButton_update.clicked.connect(self.update)
        self.pushButton_remove.clicked.connect(self.remove)
        self.set_init = var.workout_table[self.index][5]

    def update(self):
        try:
            if self.radioButton_reps.isChecked() == True:
                var.workout_table[self.index][1] = 'Reps'
                var.workout_table[self.index][2] = 0
                var.workout_table[self.index][3] = int(self.lineEdit_value.text())
                var.workout_table[self.index][4] = int(self.lineEdit_rounds.text())

            elif self.radioButton_amrap.isChecked() == True:
                var.workout_table[self.index][1] = 'AMRAP'
                var.workout_table[self.index][2] = int(self.lineEdit_time_amrap.text())
                var.workout_table[self.index][3] = int(self.lineEdit_reps_amrap.text())
                var.workout_table[self.index][4] = 0

            elif self.radioButton_reps_in_time.isChecked() == True:
                var.workout_table[self.index][1] = 'EMOM'
                var.workout_table[self.index][2] = int(self.lineEdit_time.text())
                var.workout_table[self.index][3] = int(self.lineEdit_reps.text())
                var.workout_table[self.index][4] = int(self.lineEdit_rounds.text())

            else:
                var.workout_table[self.index][1] = 'Time'
                var.workout_table[self.index][2] = int(self.lineEdit_value.text())
                var.workout_table[self.index][3] = 0
                var.workout_table[self.index][4] = int(self.lineEdit_rounds.text())

            var.workout_table[self.index][5] = self.comboBox.currentText()
            temp = var.workout_table[self.index]
            if self.set_init != var.workout_table[self.index][5]:
                var.workout_table.pop(self.index)
                sets = [var.workout_table[i][5] for i in range(len(var.workout_table))]
                if len(var.workout_table) == 0 and len(var.workout_table) == 1:
                    var.workout_table = list()
                    var.workout_table.append(var.workout_table[self.index])
                else:
                    try:
                        index = len(sets) - sets[::-1].index(temp[5])
                    except:
                        index = -1

                    if index == -1:
                        var.workout_table.append(temp)
                    else:
                        var.workout_table.insert(index, temp)
                for index, item in enumerate(var.workout_table):
                    for index1, item1 in enumerate(var.workout_table):
                        if var.workout_table[index][5]<var.workout_table[index1][5]:
                            var.workout_table[index], var.workout_table[index1] = var.workout_table[index1], var.workout_table[index]

            sets = [var.workout_table[i][5] for i in range(len(var.workout_table))]
            sets = list(set(sets))
            if len(sets)>1:
                for index, item in enumerate(var.workout_table):
                    if item[5] == temp[5]:
                        var.workout_table[index][4] = temp[4]
                if len(sets)==2:
                    key = var.workout_table[0][5]
                    for index, item in enumerate(var.workout_table):
                        if key == item[5]:
                            var.workout_table[index][4] = var.workout_table[0][4]

            if temp[1] == "AMRAP":
                if len(sets)>1:
                    for index, item in enumerate(var.workout_table):
                        if item[5] == temp[5]:
                            var.workout_table[index][2] = temp[2]
                    if len(sets)==2:
                        key = var.workout_table[0][5]
                        for index, item in enumerate(var.workout_table):
                            if key == item[5]:
                                var.workout_table[index][2] = var.workout_table[0][2]
            alert(text='Updated Succesfully', title='Alert', button='OK')
        except Exception as e:
            alert(text=('Error while Updating- {}'.format(e)), title='Alert', button='OK')

        self.Dialog.close()

    def remove(self):
        try:
            var.workout_table.pop(self.index)
            for index, item in enumerate(var.workout_table):
                for index1, item1 in enumerate(var.workout_table):
                    if var.workout_table[index][5]<var.workout_table[index1][5]:
                        var.workout_table[index], var.workout_table[index1] = var.workout_table[index1], var.workout_table[index]
            alert(text='Removed Succesfully', title='Alert', button='OK')
        except Exception as e:
            alert(text=('Error while removing - {}'.format(e)), title='Alert', button='OK')

        self.Dialog.close()


def main(index):
    dialog = QtWidgets.QDialog()
    dialog.ui = Ui_Dialog(index)
    dialog.ui.setupUi(dialog)
    return dialog.exec_()