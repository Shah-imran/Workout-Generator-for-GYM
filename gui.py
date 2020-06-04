# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1174, 764)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_search_exercise = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_search_exercise.sizePolicy().hasHeightForWidth())
        self.lineEdit_search_exercise.setSizePolicy(sizePolicy)
        self.lineEdit_search_exercise.setText("")
        self.lineEdit_search_exercise.setObjectName("lineEdit_search_exercise")
        self.gridLayout.addWidget(self.lineEdit_search_exercise, 17, 2, 1, 1)
        self.tableWidget_exercise = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.tableWidget_exercise.setFont(font)
        self.tableWidget_exercise.setStyleSheet("")
        self.tableWidget_exercise.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget_exercise.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableWidget_exercise.setLineWidth(0)
        self.tableWidget_exercise.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_exercise.setDragEnabled(False)
        self.tableWidget_exercise.setDragDropOverwriteMode(False)
        self.tableWidget_exercise.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.tableWidget_exercise.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.tableWidget_exercise.setAlternatingRowColors(True)
        self.tableWidget_exercise.setShowGrid(False)
        self.tableWidget_exercise.setGridStyle(QtCore.Qt.NoPen)
        self.tableWidget_exercise.setWordWrap(False)
        self.tableWidget_exercise.setRowCount(0)
        self.tableWidget_exercise.setColumnCount(0)
        self.tableWidget_exercise.setObjectName("tableWidget_exercise")
        self.tableWidget_exercise.horizontalHeader().setVisible(False)
        self.tableWidget_exercise.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget_exercise.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_exercise.verticalHeader().setVisible(True)
        self.tableWidget_exercise.verticalHeader().setHighlightSections(True)
        self.gridLayout.addWidget(self.tableWidget_exercise, 26, 0, 1, 2)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(48)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_print = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_print.sizePolicy().hasHeightForWidth())
        self.pushButton_print.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        self.pushButton_print.setFont(font)
        self.pushButton_print.setStyleSheet("QPushButton {\n"
"    color: #000;\n"
"    border: 1px solid #555;\n"
"    border-radius: 3px;\n"
"    border-style: Solid;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #FFF, stop: 1 #D3D3D3\n"
"        );\n"
"    padding: 5px 28px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushButton_print.setObjectName("pushButton_print")
        self.gridLayout_2.addWidget(self.pushButton_print, 3, 10, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 2, 3, 1, 1, QtCore.Qt.AlignRight)
        self.lineEdit_ip = QtWidgets.QLineEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_ip.sizePolicy().hasHeightForWidth())
        self.lineEdit_ip.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        self.lineEdit_ip.setFont(font)
        self.lineEdit_ip.setObjectName("lineEdit_ip")
        self.gridLayout_2.addWidget(self.lineEdit_ip, 2, 9, 1, 1)
        self.spinBox_print_labels = QtWidgets.QSpinBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_print_labels.sizePolicy().hasHeightForWidth())
        self.spinBox_print_labels.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.spinBox_print_labels.setFont(font)
        self.spinBox_print_labels.setMinimum(1)
        self.spinBox_print_labels.setObjectName("spinBox_print_labels")
        self.gridLayout_2.addWidget(self.spinBox_print_labels, 2, 10, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 1, 10, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 1, 9, 1, 1)
        self.lineEdit_workout_name = QtWidgets.QLineEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_workout_name.sizePolicy().hasHeightForWidth())
        self.lineEdit_workout_name.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        self.lineEdit_workout_name.setFont(font)
        self.lineEdit_workout_name.setObjectName("lineEdit_workout_name")
        self.gridLayout_2.addWidget(self.lineEdit_workout_name, 2, 0, 1, 1)
        self.pushButton_workout_save = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_workout_save.sizePolicy().hasHeightForWidth())
        self.pushButton_workout_save.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        self.pushButton_workout_save.setFont(font)
        self.pushButton_workout_save.setStyleSheet("QPushButton {\n"
"    color: #1E1E1E;\n"
"    border: 1px solid #555;\n"
"    border-radius: 3px;\n"
"    border-style: Solid;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #e5e5e5, stop: 1 #79d70f\n"
"        );\n"
"    padding: 5px 28px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushButton_workout_save.setObjectName("pushButton_workout_save")
        self.gridLayout_2.addWidget(self.pushButton_workout_save, 2, 2, 1, 1)
        self.label_save_workout = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_save_workout.sizePolicy().hasHeightForWidth())
        self.label_save_workout.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_save_workout.setFont(font)
        self.label_save_workout.setObjectName("label_save_workout")
        self.gridLayout_2.addWidget(self.label_save_workout, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 31, 0, 1, 5)
        self.pushButton_preset_workouts = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_preset_workouts.sizePolicy().hasHeightForWidth())
        self.pushButton_preset_workouts.setSizePolicy(sizePolicy)
        self.pushButton_preset_workouts.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        self.pushButton_preset_workouts.setFont(font)
        self.pushButton_preset_workouts.setStyleSheet("QPushButton {\n"
"    color: #000;\n"
"    border: 1px solid #555;\n"
"    border-radius: 3px;\n"
"    border-style: Solid;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #FFF, stop: 1 #D3D3D3\n"
"        );\n"
"    padding: 5px 28px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushButton_preset_workouts.setObjectName("pushButton_preset_workouts")
        self.gridLayout.addWidget(self.pushButton_preset_workouts, 17, 1, 1, 1)
        self.pushButton_logout = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_logout.sizePolicy().hasHeightForWidth())
        self.pushButton_logout.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        self.pushButton_logout.setFont(font)
        self.pushButton_logout.setStyleSheet("QPushButton {\n"
"    color: #1E1E1E;\n"
"    border: 1px solid #555;\n"
"    border-radius: 3px;\n"
"    border-style: Solid;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #e5e5e5, stop: 1 #79d70f\n"
"        );\n"
"    padding: 5px 28px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushButton_logout.setObjectName("pushButton_logout")
        self.gridLayout.addWidget(self.pushButton_logout, 14, 4, 1, 1, QtCore.Qt.AlignRight)
        self.label_table_1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_table_1.setFont(font)
        self.label_table_1.setText("")
        self.label_table_1.setObjectName("label_table_1")
        self.gridLayout.addWidget(self.label_table_1, 21, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(36)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet("background-color: rgb(198, 198, 198);")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButton_remove_muscle_groups = QtWidgets.QPushButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        self.pushButton_remove_muscle_groups.setFont(font)
        self.pushButton_remove_muscle_groups.setStyleSheet("QPushButton {\n"
"    color: #1E1E1E;\n"
"    border: 1px solid #555;\n"
"    border-radius: 3px;\n"
"    border-style: Solid;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #e5e5e5, stop: 1 #79d70f\n"
"        );\n"
"    padding: 5px 28px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushButton_remove_muscle_groups.setObjectName("pushButton_remove_muscle_groups")
        self.gridLayout_4.addWidget(self.pushButton_remove_muscle_groups, 0, 0, 1, 1, QtCore.Qt.AlignRight)
        self.pushButton_add_exercise = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_add_exercise.sizePolicy().hasHeightForWidth())
        self.pushButton_add_exercise.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        self.pushButton_add_exercise.setFont(font)
        self.pushButton_add_exercise.setStyleSheet("QPushButton {\n"
"    color: #1E1E1E;\n"
"    border: 1px solid #555;\n"
"    border-radius: 3px;\n"
"    border-style: Solid;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #e5e5e5, stop: 1 #79d70f\n"
"        );\n"
"    padding: 5px 28px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushButton_add_exercise.setObjectName("pushButton_add_exercise")
        self.gridLayout_4.addWidget(self.pushButton_add_exercise, 0, 2, 1, 1, QtCore.Qt.AlignLeft)
        self.pushButton_add_new_muscle_groups = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_add_new_muscle_groups.sizePolicy().hasHeightForWidth())
        self.pushButton_add_new_muscle_groups.setSizePolicy(sizePolicy)
        self.pushButton_add_new_muscle_groups.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        self.pushButton_add_new_muscle_groups.setFont(font)
        self.pushButton_add_new_muscle_groups.setStyleSheet("QPushButton {\n"
"    color: #1E1E1E;\n"
"    border: 1px solid #555;\n"
"    border-radius: 3px;\n"
"    border-style: Solid;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #e5e5e5, stop: 1 #79d70f\n"
"        );\n"
"    padding: 5px 28px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushButton_add_new_muscle_groups.setObjectName("pushButton_add_new_muscle_groups")
        self.gridLayout_4.addWidget(self.pushButton_add_new_muscle_groups, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout.addWidget(self.groupBox_3, 28, 0, 2, 2)
        self.pushButton_find = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_find.sizePolicy().hasHeightForWidth())
        self.pushButton_find.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        self.pushButton_find.setFont(font)
        self.pushButton_find.setStyleSheet("QPushButton {\n"
"    color: #000;\n"
"    border: 1px solid #555;\n"
"    border-radius: 3px;\n"
"    border-style: Solid;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #FFF, stop: 1 #D3D3D3\n"
"        );\n"
"    padding: 5px 28px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushButton_find.setObjectName("pushButton_find")
        self.gridLayout.addWidget(self.pushButton_find, 17, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.comboBox_exercise = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_exercise.sizePolicy().hasHeightForWidth())
        self.comboBox_exercise.setSizePolicy(sizePolicy)
        self.comboBox_exercise.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        self.comboBox_exercise.setFont(font)
        self.comboBox_exercise.setObjectName("comboBox_exercise")
        self.gridLayout.addWidget(self.comboBox_exercise, 17, 0, 1, 1)
        self.pushButton_exercise = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_exercise.sizePolicy().hasHeightForWidth())
        self.pushButton_exercise.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        self.pushButton_exercise.setFont(font)
        self.pushButton_exercise.setStyleSheet("QPushButton {\n"
"    color: #000;\n"
"    border: 1px solid #555;\n"
"    border-radius: 3px;\n"
"    border-style: Solid;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #FFF, stop: 1 #D3D3D3\n"
"        );\n"
"    padding: 5px 28px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushButton_exercise.setObjectName("pushButton_exercise")
        self.gridLayout.addWidget(self.pushButton_exercise, 21, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 14, 0, 1, 1)
        self.pushButton_exercise_clear = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_exercise_clear.sizePolicy().hasHeightForWidth())
        self.pushButton_exercise_clear.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        self.pushButton_exercise_clear.setFont(font)
        self.pushButton_exercise_clear.setStyleSheet("QPushButton {\n"
"    color: #000;\n"
"    border: 1px solid #555;\n"
"    border-radius: 3px;\n"
"    border-style: Solid;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #FFF, stop: 1 #D3D3D3\n"
"        );\n"
"    padding: 5px 28px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushButton_exercise_clear.setObjectName("pushButton_exercise_clear")
        self.gridLayout.addWidget(self.pushButton_exercise_clear, 17, 4, 1, 1, QtCore.Qt.AlignHCenter)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(36)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("background-color: rgb(198, 198, 198);")
        self.groupBox.setTitle("")
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.pushButton_set_clear = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_set_clear.sizePolicy().hasHeightForWidth())
        self.pushButton_set_clear.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        self.pushButton_set_clear.setFont(font)
        self.pushButton_set_clear.setStyleSheet("QPushButton {\n"
"    color: #000;\n"
"    border: 1px solid #555;\n"
"    border-radius: 3px;\n"
"    border-style: Solid;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #FFF, stop: 1 #D3D3D3\n"
"        );\n"
"    padding: 5px 28px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushButton_set_clear.setObjectName("pushButton_set_clear")
        self.gridLayout_3.addWidget(self.pushButton_set_clear, 2, 5, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 2, 4, 1, 1, QtCore.Qt.AlignRight)
        self.spinBox_set = QtWidgets.QSpinBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_set.sizePolicy().hasHeightForWidth())
        self.spinBox_set.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        self.spinBox_set.setFont(font)
        self.spinBox_set.setMinimum(1)
        self.spinBox_set.setProperty("value", 1)
        self.spinBox_set.setObjectName("spinBox_set")
        self.gridLayout_3.addWidget(self.spinBox_set, 2, 3, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 28, 2, 2, 3)
        self.pushButton_admin = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_admin.sizePolicy().hasHeightForWidth())
        self.pushButton_admin.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        self.pushButton_admin.setFont(font)
        self.pushButton_admin.setStyleSheet("QPushButton {\n"
"    color: #1E1E1E;\n"
"    border: 1px solid #555;\n"
"    border-radius: 3px;\n"
"    border-style: Solid;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #e5e5e5, stop: 1 #79d70f\n"
"        );\n"
"    padding: 5px 28px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushButton_admin.setObjectName("pushButton_admin")
        self.gridLayout.addWidget(self.pushButton_admin, 0, 4, 1, 1, QtCore.Qt.AlignRight)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setStyleSheet("image url(:/newPrefix/rsz_rf_logo_big (1).png)")
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(":/newPrefix/rsz_rf_logo_big (1).png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 1)
        self.tableWidget_workout = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.tableWidget_workout.setFont(font)
        self.tableWidget_workout.setMouseTracking(True)
        self.tableWidget_workout.setStyleSheet("")
        self.tableWidget_workout.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget_workout.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tableWidget_workout.setLineWidth(1)
        self.tableWidget_workout.setMidLineWidth(0)
        self.tableWidget_workout.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_workout.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.tableWidget_workout.setAlternatingRowColors(False)
        self.tableWidget_workout.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_workout.setShowGrid(True)
        self.tableWidget_workout.setObjectName("tableWidget_workout")
        self.tableWidget_workout.setColumnCount(0)
        self.tableWidget_workout.setRowCount(0)
        self.tableWidget_workout.horizontalHeader().setVisible(True)
        self.tableWidget_workout.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_workout.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget_workout.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.tableWidget_workout, 26, 2, 1, 3)
        self.pushButton_about = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_about.sizePolicy().hasHeightForWidth())
        self.pushButton_about.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        self.pushButton_about.setFont(font)
        self.pushButton_about.setStyleSheet("QPushButton {\n"
"    color: #1E1E1E;\n"
"    border: 1px solid #555;\n"
"    border-radius: 3px;\n"
"    border-style: Solid;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #e5e5e5, stop: 1 #79d70f\n"
"        );\n"
"    padding: 5px 28px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        self.pushButton_about.setObjectName("pushButton_about")
        self.gridLayout.addWidget(self.pushButton_about, 0, 3, 1, 1, QtCore.Qt.AlignHCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Workout Generator"))
        self.lineEdit_search_exercise.setPlaceholderText(_translate("MainWindow", "search exercise"))
        self.pushButton_print.setText(_translate("MainWindow", "Print"))
        self.label_5.setText(_translate("MainWindow", "Print your workout"))
        self.label_7.setText(_translate("MainWindow", "# of prints"))
        self.label_6.setText(_translate("MainWindow", "Printer IP"))
        self.lineEdit_workout_name.setPlaceholderText(_translate("MainWindow", "Name of Workout"))
        self.pushButton_workout_save.setText(_translate("MainWindow", "Save"))
        self.label_save_workout.setText(_translate("MainWindow", "Save Workout"))
        self.pushButton_preset_workouts.setText(_translate("MainWindow", "Preset workouts"))
        self.pushButton_logout.setText(_translate("MainWindow", "Logout"))
        self.pushButton_remove_muscle_groups.setText(_translate("MainWindow", "Remove Muscle Groups"))
        self.pushButton_add_exercise.setText(_translate("MainWindow", "Add exercise"))
        self.pushButton_add_new_muscle_groups.setText(_translate("MainWindow", "Add New Muscle Groups"))
        self.pushButton_find.setText(_translate("MainWindow", "Search"))
        self.pushButton_exercise.setText(_translate("MainWindow", "Exercise"))
        self.label.setText(_translate("MainWindow", "Select a muscle groups"))
        self.pushButton_exercise_clear.setText(_translate("MainWindow", "Clear"))
        self.label_9.setText(_translate("MainWindow", " Total Sets in this Workout "))
        self.pushButton_set_clear.setText(_translate("MainWindow", "Clear"))
        self.label_10.setText(_translate("MainWindow", "    Clear all exercises in this workout "))
        self.pushButton_admin.setText(_translate("MainWindow", "Admin"))
        self.pushButton_about.setText(_translate("MainWindow", "About"))
import logo_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
