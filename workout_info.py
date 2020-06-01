# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'workout_info.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import db

class Ui_Dialog(object):
    def __init__(self, name, exercise_name, info, sets, types, calories, exercise_time, workout_time, reps, rounds):
        self.name = name
        self.exercise_name = exercise_name
        self.info = info
        self.sets = sets
        self.types = types
        self.calories = calories
        self.exercise_time = exercise_time
        self.workout_time = workout_time
        self.reps = reps
        self.rounds = rounds

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(738, 600)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        Dialog.setFont(font)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textBrowser_left = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_left.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_left.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.textBrowser_left.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.textBrowser_left.setObjectName("textBrowser_left")
        self.horizontalLayout.addWidget(self.textBrowser_left)
        self.textBrowser_right = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_right.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_right.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.textBrowser_right.setObjectName("textBrowser_right")
        self.horizontalLayout.addWidget(self.textBrowser_right)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Info: {}".format(self.name)))
        calories = 0
        try:
            for count in range(len(self.exercise_name)):
                if self.types[count] == "Time":
                    calories += (self.calories[count] * self.rounds[count] * (self.workout_time[count]/self.exercise_time[count]))
                else:
                    calories += (self.calories[count] * self.rounds[count] * self.reps[count])
        except:
            pass

        time = 0
        for count in range(len(self.exercise_name)):
            if self.types[count] == "Reps":
                time += (self.reps[count] * self.rounds[count] * self.exercise_time[count])
            else:
                time += (self.workout_time[count] * self.rounds[count])


        left = """Calories: {}\nTotal Workout Time: {} min\n\n{}""".format(calories, time/60, self.info)
        self.textBrowser_left.setText(_translate("Dialog", "{}".format(left)))

        right = """Exercises:\n\n"""
        if len(set(self.sets)) > 1:
            sets = list(set(self.sets))
            for item in sets:
                right += "Set " + str(item) + "\n\n"

                for name, v_type, time, reps, w_set, rounds in zip(self.exercise_name, self.types, self.workout_time, self.reps, self.sets, self.rounds):
                    if w_set == item:
                        right += name
                        if v_type == "Time":
                            right += "  {} seconds\n".format(str(time)).rjust(30 - len(name))
                        elif v_type == "EMOM":
                            right += "  {} reps in {} seconds\n".format(reps, time).rjust(40 - len(name))
                        else:
                            right += "  {} reps\n".format(str(reps)).rjust(30 - len(name))
                        round = rounds
                right += "\nRepeat: " + str(round) + " rounds\n"
                right += "________________________________\n\n"
        else:
            for name, v_type, time, reps, round in zip(self.exercise_name, self.types, self.workout_time, self.reps, self.rounds):
                right += name
                if v_type == "Time":
                    right += "  {} seconds {} rounds\n".format(str(time), str(round)).rjust(30 - len(name))
                elif v_type == "EMOM":
                    right += "  {} reps in {} seconds {} rounds\n".format(reps, time, round).rjust(40 - len(name))
                else:
                    right += "  {} reps {} rounds\n".format(str(reps), str(round)).rjust(30 - len(name))
        print(right)
        self.textBrowser_right.setText(_translate("Dialog", "{}".format(right)))
        # for item in right.split("\n"):
        #     print(item)
        #     item = '<span style=\" color: #000;\">%s</span>' % item.replace(" ","&nbsp;")
        #     print(item)
        #     self.textBrowser_right.append(item)


def main(name):
    conn = db.DB()
    exercise_name, info, sets, types, calories, exercise_time, workout_time, reps, rounds = conn.fetch_workout_info(name)
    conn.close()
    dialog = QtWidgets.QDialog()
    dialog.ui = Ui_Dialog(name, exercise_name, info, sets, types, calories, exercise_time, workout_time, reps, rounds)
    dialog.ui.setupUi(dialog)
    return dialog.exec_()