# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'exercise_info.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import db


class Ui_Dialog(object):

    def __init__(self, name, info, groups, image_path):
        self.name =  name
        self.info = info
        self.groups = groups
        self.image_path = image_path

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(501, 373)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_muscle_groups = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_muscle_groups.setFont(font)
        self.label_muscle_groups.setObjectName("label_muscle_groups")
        self.verticalLayout.addWidget(self.label_muscle_groups)
        self.label_info = QtWidgets.QLabel(Dialog)
        self.label_info.setWordWrap(True)
        self.label_info.setObjectName("label_info")
        self.verticalLayout.addWidget(self.label_info)
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setStyleSheet("background-color: #F0F0F0;")
        self.graphicsView.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Info: {}".format(self.name)))
        self.label_muscle_groups.setText(_translate("Dialog", "Muscle Group(s): {}".format(self.groups)))
        self.label_info.setText(_translate("Dialog", "{}".format(self.info)))

        scene = Qt.QGraphicsScene()
        pix = Qt.QPixmap(self.image_path).scaled(445, 400, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
        scene.addPixmap(pix)
        self.graphicsView.setScene(scene)
        self.graphicsView.show()

def main(name):
    conn = db.DB()
    info, groups, image_path = conn.fetch_exercise_info(name)
    conn.close()
    dialog = QtWidgets.QDialog()
    groups = list(set(groups))
    groups = ','.join(groups)
    dialog.ui = Ui_Dialog(name, info, groups, image_path)
    dialog.ui.setupUi(dialog)
    return dialog.exec_()

