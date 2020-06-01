# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'remove_muscle_groups.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import var, db


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(310, 544)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        Dialog.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.tableWidget.setFont(font)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(130)
        self.tableWidget.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Remove Muscle Groups"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Muscle Groups"))
        self.show()
    def show(self):
        try:
            con = db.DB()
            result = con.fetch_muscle_groups()
            result = list(result)
            con.close()
            print(result)
            self.tableWidget.setRowCount(len(result))
            for row in range(0,len(result)):
                self.tableWidget.setItem(row,0, QTableWidgetItem(str(result[row])))
                button_delete = QtWidgets.QPushButton('Delete')
                button_delete.clicked.connect(self.delete)
                button_delete.setStyleSheet(var.button_style)
                button_delete.setIcon(QtGui.QIcon(var.delete_icon))
                self.tableWidget.setCellWidget(row,1,button_delete)
        except Exception as e:
            print('Exception at remove_muscle - {}'.format(e))

    def delete(self):
        try:
            row = self.get_index_of_button(self.tableWidget)
            name = self.tableWidget.item(row, 0).text()
            conn = db.DB()
            result = conn.remove_muscle_groups(name)
            self.show()
        except Exception as e:
            print("Error at remove muscle db - {}".format(e))

    def get_index_of_button(self, table):

        button = QtWidgets.qApp.focusWidget()
        # or button = self.sender()
        index = table.indexAt(button.pos())
        if index.isValid():
            # print(index.row(), index.column())
            return index.row()


def main():
    dialog = QtWidgets.QDialog()
    dialog.ui = Ui_Dialog()
    dialog.ui.setupUi(dialog)
    return dialog.exec_()
