import datetime
from escpos.printer import Network
import edit_exercise as ee
import remove_muscle_groups as rmg
import save_workout as sw
import update_workout as uw
import add_to_workout as atw
import workout_info as wi
import add_exercise as ae
import exercise_info as ei
import about
from pyautogui import alert, password, confirm
import add_muscle as am
import db
import json
from threading import Thread
from time import sleep
import var
import os
import sys
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from gui import Ui_MainWindow
import encodings.idna
print("App started....")


class MyGui(Ui_MainWindow, QtWidgets.QWidget):
    def __init__(self, mainWindow):
        Ui_MainWindow.__init__(self)
        QtWidgets.QWidget.__init__(self)
        self.setupUi(mainWindow)


button_style = var.button_style


class myMainClass():
    def __init__(self):
        GUI.lineEdit_ip.setText(var.printer_ip)
        Thread(target=show_muscle_groups, daemon=True).start()
        GUI.comboBox_exercise.currentIndexChanged.connect(self.show_exercises)

        GUI.pushButton_add_new_muscle_groups.clicked.connect(add_muscle)
        GUI.pushButton_add_exercise.clicked.connect(self.add_exercise)
        GUI.pushButton_add_new_muscle_groups.setIcon(QtGui.QIcon(var.add_icon))
        GUI.pushButton_add_exercise.setIcon(QtGui.QIcon(var.add_icon))

        GUI.pushButton_find.clicked.connect(self.search_results)
        GUI.pushButton_find.setIcon(QtGui.QIcon(var.search_icon))

        GUI.pushButton_exercise_clear.clicked.connect(self.exercise_clear)
        GUI.pushButton_exercise_clear.setIcon(QtGui.QIcon(var.cancel_icon))

        GUI.pushButton_exercise.clicked.connect(self.show_exercises)
        GUI.pushButton_logout.clicked.connect(self.hide)
        GUI.pushButton_logout.setIcon(QtGui.QIcon(var.logout_icon))

        GUI.pushButton_admin.clicked.connect(self.check_password)
        GUI.pushButton_admin.setIcon(QtGui.QIcon(var.admin_icon))
        GUI.pushButton_preset_workouts.clicked.connect(self.show_preset)

        GUI.tableWidget_workout.setEditTriggers(
            QtWidgets.QTableWidget.NoEditTriggers)
        GUI.tableWidget_exercise.setEditTriggers(
            QtWidgets.QTableWidget.NoEditTriggers)

        GUI.pushButton_print.clicked.connect(self.print_workout)
        GUI.pushButton_print.setIcon(QtGui.QIcon(var.print_icon))
        self.hide()

        GUI.pushButton_set_clear.clicked.connect(self.workout_clear)
        GUI.pushButton_set_clear.setIcon(QtGui.QIcon(var.cancel_icon))

        GUI.pushButton_workout_save.clicked.connect(self.save_workout)
        GUI.pushButton_workout_save.setIcon(QtGui.QIcon(var.save_icon))

        GUI.pushButton_remove_muscle_groups.clicked.connect(
            self.remove_muscle_groups)
        GUI.pushButton_remove_muscle_groups.setIcon(
            QtGui.QIcon(var.delete_icon))
        GUI.pushButton_about.setIcon(QtGui.QIcon(var.about_icon))
        GUI.pushButton_about.clicked.connect(self.about)

    def about(self):
        about.main()

    def remove_muscle_groups(self):
        rmg.main()
        Thread(target=show_muscle_groups, daemon=True).start()

    def exercise_clear(self):
        GUI.lineEdit_search_exercise.clear()
        self.show_exercises()

    def print_workout(self):
        Thread(target=print_workout, daemon=True).start()

    def save_workout(self):
        name = GUI.lineEdit_workout_name.text()
        sw.main(name)
        self.show_preset()

    def workout_clear(self):
        result = confirm(text='Are you sure?',
                         title='Clear Workout Table', buttons=['OK', 'Cancel'])
        if result == "OK":
            GUI.tableWidget_workout.setRowCount(0)
            var.workout_table = list()
            self.show_workout()
        else:
            pass

    def add_set(self):
        var.set_count = GUI.spinBox_set.value()
        print(var.set_count)

    def show_preset(self):
        try:
            GUI.tableWidget_exercise.setRowCount(0)
            conn = db.DB()
            result = conn.fetch_workout_name()
            conn.close()
            result = list(set(result))
            print(result)
            GUI.tableWidget_exercise.setRowCount(len(result))
            if var.admin_mode == True:
                GUI.tableWidget_exercise.setColumnCount(4)
            else:
                GUI.tableWidget_exercise.setColumnCount(3)
            GUI.label_table_1.setText("Preset Workouts")
            result = sorted(result, key=len)

            for row in range(0, len(result)):
                GUI.tableWidget_exercise.setItem(
                    row, 0, QTableWidgetItem(str(result[row])))
                button_info = QtWidgets.QPushButton('Info')
                button_info.setStyleSheet(button_style)
                button_info.clicked.connect(self.show_workout_info)
                button_info.setIcon(QtGui.QIcon(var.info_icon))
                GUI.tableWidget_exercise.setCellWidget(row, 1, button_info)
                button_add = QtWidgets.QPushButton('Add')
                button_add.setStyleSheet(button_style)
                button_add.clicked.connect(self.add_preset_to_workout)
                button_add.setIcon(QtGui.QIcon(var.add_icon))
                GUI.tableWidget_exercise.setCellWidget(row, 2, button_add)
                if var.admin_mode == True:
                    button_remove = QtWidgets.QPushButton('Delete')
                    button_remove.setStyleSheet(button_style)
                    button_remove.clicked.connect(self.remove_workout)
                    button_remove.setIcon(QtGui.QIcon(var.delete_icon))
                    GUI.tableWidget_exercise.setCellWidget(
                        row, 3, button_remove)
                GUI.tableWidget_exercise.resizeColumnsToContents()
        except Exception as e:
            print("error at show_preset table - {}".format(e))

    def remove_workout(self):
        try:
            row, column = self.get_index_of_button(GUI.tableWidget_exercise)
            name = GUI.tableWidget_exercise.item(row, 0).text()
            result = confirm(text='Are you sure?',
                             title='Delete Workout', buttons=['OK', 'Cancel'])
            if result == "OK":
                conn = db.DB()
                conn.remove_workout(name)
                conn.close()
            else:
                pass
            self.show_preset()
        except:
            pass

    def add_preset_to_workout(self):
        try:
            row, column = self.get_index_of_button(GUI.tableWidget_exercise)
            name = GUI.tableWidget_exercise.item(row, 0).text()
            result = confirm(text='This will reset workout table.\nAre you sure?',
                             title='Add new workout', buttons=['OK', 'Cancel'])
            if result == "OK":
                conn = db.DB()
                exercise_name, info, w_sets, types, calories, exercise_time, workout_time, reps, rounds = conn.fetch_workout_info(
                    name)
                var.workout_table = list()
                for count in range(len(w_sets)):
                    # if types[count] == "time":
                    temp = [exercise_name[count], types[count], workout_time[count],
                            reps[count], rounds[count], "Set {}".format(w_sets[count])]
                    # else:
                    #     temp = [exercise_name[count], types[count], reps[count], rounds[count], "Set {}".format(w_sets[count])]

                    if len(var.workout_table) == 0 and len(var.workout_table) == 1:
                        var.workout_table.append(temp)
                    else:
                        sets = [var.workout_table[i][5]
                                for i in range(len(var.workout_table))]
                        try:
                            index = len(sets) - sets[::-1].index(temp[5])
                        except:
                            index = -1

                        if index == -1:
                            var.workout_table.append(temp)
                        else:
                            var.workout_table.insert(index, temp)
                sets = [var.workout_table[i][5]
                        for i in range(len(var.workout_table))]
                GUI.spinBox_set.setValue(len(list(set(sets))))
                self.show_workout()
        except Exception as e:
            print("error at add_preset_to_workout - {}".format(e))

    def show_workout_info(self):
        row, column = self.get_index_of_button(GUI.tableWidget_exercise)
        name = GUI.tableWidget_exercise.item(row, 0).text()
        wi.main(name)

    def hide(self):
        GUI.pushButton_add_new_muscle_groups.hide()
        GUI.pushButton_add_exercise.hide()
        GUI.pushButton_logout.hide()
        GUI.pushButton_admin.show()
        GUI.pushButton_workout_save.hide()
        GUI.lineEdit_workout_name.hide()
        GUI.label_save_workout.hide()
        GUI.pushButton_remove_muscle_groups.hide()
        var.admin_mode = False
        Thread(target=show_muscle_groups, daemon=True).start()
        self.show_exercises()
        GUI.tableWidget_workout.setRowCount(0)
        var.workout_table = list()
        self.show_workout()

    def show(self):
        GUI.pushButton_add_new_muscle_groups.show()
        GUI.pushButton_add_exercise.show()
        GUI.pushButton_logout.show()
        GUI.pushButton_admin.hide()
        GUI.pushButton_workout_save.show()
        GUI.lineEdit_workout_name.show()
        GUI.label_save_workout.show()
        GUI.pushButton_remove_muscle_groups.show()
        GUI.pushButton_admin.setEnabled(True)
        var.admin_mode = True
        Thread(target=show_muscle_groups, daemon=True).start()
        self.show_exercises()

    def check_password(self):
        GUI.pushButton_admin.setEnabled(False)
        admin_password = password(
            text='enter admin password', title='Password', default='', mask='*')

        if admin_password == var.admin_password:
            alert(text='Logged in...', title='Alert', button='OK')
            self.show()

        elif admin_password == "" or admin_password == None:
            alert(text='Nothing entered', title='Alert', button='OK')
            GUI.pushButton_admin.setEnabled(True)

        else:
            alert(text='Wrong Password!!!', title='Alert', button='OK')
            GUI.pushButton_admin.setEnabled(True)

    def search_results(self):
        try:
            keyword = GUI.lineEdit_search_exercise.text()

            print("Search keyword - {}".format(keyword))

            conn = db.DB()
            result = conn.search_exercise(keyword)
            conn.close()
            result = list(set(result))
            print(result)
            GUI.tableWidget_exercise.setRowCount(len(result))
            GUI.tableWidget_exercise.setColumnCount(3)
            GUI.label_table_1.setText("Search result for: {}".format(keyword))
            result = sorted(result, key=len)
            for row in range(0, len(result)):
                GUI.tableWidget_exercise.setItem(
                    row, 0, QTableWidgetItem(str(result[row])))
                button_info = QtWidgets.QPushButton('Info')
                button_info.clicked.connect(self.show_info)
                button_info.setIcon(QtGui.QIcon(var.info_icon))
                GUI.tableWidget_exercise.setCellWidget(row, 1, button_info)
                button_add = QtWidgets.QPushButton('Add')
                button_add.clicked.connect(self.add_exercise_to_workout)
                button_add.setIcon(QtGui.QIcon(var.add_icon))
                GUI.tableWidget_exercise.setCellWidget(row, 2, button_add)
                if var.admin_mode == True:
                    button_remove = QtWidgets.QPushButton('Delete')
                    button_remove.setStyleSheet(button_style)
                    button_remove.clicked.connect(self.remove_exercise)
                    button_remove.setIcon(QtGui.QIcon(var.delete_icon))
                    GUI.tableWidget_exercise.setCellWidget(
                        row, 4, button_remove)
                    button_edit = QtWidgets.QPushButton(' Edit ')
                    button_edit.setStyleSheet(button_style)
                    button_edit.clicked.connect(self.edit_exercise)
                    button_edit.setIcon(QtGui.QIcon(var.edit_icon))
                    GUI.tableWidget_exercise.setCellWidget(row, 3, button_edit)
                GUI.tableWidget_exercise.resizeColumnsToContents()
        except Exception as e:
            print("error at show_eercise table - {}".format(e))

    def show_exercises(self):
        try:
            GUI.tableWidget_exercise.setRowCount(0)
            keyword = GUI.comboBox_exercise.currentText()

            if keyword == "ALL":
                keyword = '1" OR "1" = "1'

            print(keyword)
            con = db.DB()
            result = con.fetch_exercise(keyword)
            con.close()
            result = list(set(result))
            print(result)
            GUI.tableWidget_exercise.setRowCount(len(result))
            if var.admin_mode == True:
                GUI.tableWidget_exercise.setColumnCount(5)
            else:
                GUI.tableWidget_exercise.setColumnCount(3)
            GUI.label_table_1.setText("Exercise for: {}".format(
                GUI.comboBox_exercise.currentText()))
            result.sort()

            for row in range(0, len(result)):
                GUI.tableWidget_exercise.setItem(
                    row, 0, QTableWidgetItem(str(result[row])))
                button_info = QtWidgets.QPushButton('Info')
                button_info.clicked.connect(self.show_info)
                button_info.setStyleSheet(button_style)
                button_info.setIcon(QtGui.QIcon(var.info_icon))
                GUI.tableWidget_exercise.setCellWidget(row, 1, button_info)
                button_add = QtWidgets.QPushButton('Add')
                button_add.setStyleSheet(button_style)
                button_add.clicked.connect(self.add_exercise_to_workout)
                button_add.setIcon(QtGui.QIcon(var.add_icon))
                GUI.tableWidget_exercise.setCellWidget(row, 2, button_add)
                if var.admin_mode == True:
                    button_remove = QtWidgets.QPushButton('Delete')
                    button_remove.setStyleSheet(button_style)
                    button_remove.clicked.connect(self.remove_exercise)
                    button_remove.setIcon(QtGui.QIcon(var.delete_icon))
                    GUI.tableWidget_exercise.setCellWidget(
                        row, 4, button_remove)
                    button_edit = QtWidgets.QPushButton(' Edit ')
                    button_edit.setStyleSheet(button_style)
                    button_edit.clicked.connect(self.edit_exercise)
                    button_edit.setIcon(QtGui.QIcon(var.edit_icon))
                    GUI.tableWidget_exercise.setCellWidget(row, 3, button_edit)
                GUI.tableWidget_exercise.resizeColumnsToContents()
        except Exception as e:
            print("error at show_exercise table - {}".format(e))

    def edit_exercise(self):
        row, column = self.get_index_of_button(GUI.tableWidget_exercise)
        name = GUI.tableWidget_exercise.item(row, 0).text()
        ee.main(name)
        self.show_exercises()

    def remove_exercise(self):
        try:
            row, column = self.get_index_of_button(GUI.tableWidget_exercise)
            name = GUI.tableWidget_exercise.item(row, 0).text()
            result = confirm(text='Are you sure?',
                             title='Delete Exercise', buttons=['OK', 'Cancel'])
            if result == "OK":
                conn = db.DB()
                conn.remove_exercise(name)
                conn.close()
            else:
                pass
            self.show_exercises()
        except:
            pass

    def show_info(self):
        row, column = self.get_index_of_button(GUI.tableWidget_exercise)
        name = GUI.tableWidget_exercise.item(row, 0).text()
        ei.main(name)

    def add_exercise_to_workout(self):
        var.set_count = GUI.spinBox_set.value()
        row, column = self.get_index_of_button(GUI.tableWidget_exercise)
        name = GUI.tableWidget_exercise.item(row, 0).text()
        atw.main(name)
        self.show_workout()

    def show_workout(self):
        sets = [var.workout_table[i][5] for i in range(len(var.workout_table))]
        sets = list(set(sets))

        if len(sets) == 1:
            GUI.tableWidget_workout.setRowCount(0)
            GUI.tableWidget_workout.setRowCount(len(var.workout_table))
            GUI.tableWidget_workout.setColumnCount(8)
            GUI.tableWidget_workout.setHorizontalHeaderLabels(
                ["Exercise", "Type", "Time", "Reps", "Rounds", "", "", ""])
            for row in range(len(var.workout_table)):
                for col in range(5):
                    if var.workout_table[row][col] != 0:
                        GUI.tableWidget_workout.setItem(row, col, QTableWidgetItem(
                            str("  "+str(var.workout_table[row][col]))+" "))
                    else:
                        GUI.tableWidget_workout.setItem(
                            row, col, QTableWidgetItem(str("  ")))
                    GUI.tableWidget_workout.resizeColumnsToContents()
                button_edit = QtWidgets.QPushButton(' Edit ')
                button_edit.setStyleSheet(button_style)
                button_edit.clicked.connect(self.edit)
                button_edit.setIcon(QtGui.QIcon(var.edit_icon))
                GUI.tableWidget_workout.setCellWidget(row, 5, button_edit)
                button_up = QtWidgets.QPushButton('')
                button_up.setStyleSheet(button_style)
                button_up.clicked.connect(self.move_up)
                button_up.setIcon(QtGui.QIcon(var.move_up_icon))
                GUI.tableWidget_workout.setCellWidget(row, 6, button_up)
                button_down = QtWidgets.QPushButton('')
                button_down.setStyleSheet(button_style)
                button_down.clicked.connect(self.move_down)
                button_down.setIcon(QtGui.QIcon(var.move_down_icon))
                GUI.tableWidget_workout.setCellWidget(row, 7, button_down)
                GUI.tableWidget_workout.resizeColumnsToContents()
                GUI.tableWidget_workout.showGrid()

        elif len(sets) > 1:
            # for index, item in enumerate(var.workout_table):
            #     for index1, item1 in enumerate(var.workout_table):
            #         if var.workout_table[index][5]<var.workout_table[index1][5]:
            #             var.workout_table[index], var.workout_table[index1] = var.workout_table[index1], var.workout_table[index]

            GUI.tableWidget_workout.setRowCount(0)
            GUI.tableWidget_workout.setRowCount(len(var.workout_table))
            GUI.tableWidget_workout.setColumnCount(9)
            GUI.tableWidget_workout.setHorizontalHeaderLabels(
                ["Exercise", "Type", "Time", "Reps", "Rounds", "Set", "", "", ""])
            track = var.workout_table[0][5]
            color1 = (255, 255, 255)
            color2 = (220, 220, 220)
            for row in range(len(var.workout_table)):
                if track == var.workout_table[row][5]:
                    color = color1
                else:
                    track = var.workout_table[row][5]
                    color = color2
                    color1, color2 = color2, color1
                for col in range(6):
                    if var.workout_table[row][col] != 0:
                        GUI.tableWidget_workout.setItem(row, col, QTableWidgetItem(
                            str("  "+str(var.workout_table[row][col]))+" "))
                    else:
                        GUI.tableWidget_workout.setItem(
                            row, col, QTableWidgetItem(str("  ")))
                    GUI.tableWidget_workout.resizeColumnsToContents()
                    GUI.tableWidget_workout.item(row, col).setBackground(
                        QtGui.QColor(color[0], color[1], color[2]))

                button_edit = QtWidgets.QPushButton(' Edit ')
                button_edit.setStyleSheet(button_style)
                button_edit.clicked.connect(self.edit)
                button_edit.setIcon(QtGui.QIcon(var.edit_icon))
                GUI.tableWidget_workout.setCellWidget(row, 6, button_edit)
                button_up = QtWidgets.QPushButton('')
                button_up.setStyleSheet(button_style)
                button_up.clicked.connect(self.move_up)
                button_up.setIcon(QtGui.QIcon(var.move_up_icon))
                GUI.tableWidget_workout.setCellWidget(row, 7, button_up)
                button_down = QtWidgets.QPushButton('')
                button_down.setStyleSheet(button_style)
                button_down.clicked.connect(self.move_down)
                button_down.setIcon(QtGui.QIcon(var.move_down_icon))
                GUI.tableWidget_workout.setCellWidget(row, 8, button_down)
                GUI.tableWidget_workout.resizeColumnsToContents()
                GUI.tableWidget_workout.showGrid()

        else:
            GUI.tableWidget_workout.setRowCount(0)

    def move_down(self):
        print("down")
        try:
            if len(var.workout_table) > 1:
                row, column = self.get_index_of_button(GUI.tableWidget_workout)
                if var.workout_table[row][5] == var.workout_table[row+1][5] and row != len(var.workout_table)-1:
                    var.workout_table[row], var.workout_table[row+1] = var.workout_table[row+1], var.workout_table[row]
                    self.show_workout()
                else:
                    alert(text='Can\'t move', title='Alert', button='OK')
        except Exception as e:
            alert(text='Can\'t move', title='Alert', button='OK')
            print("Can't Move")

    def move_up(self):
        print("up")
        try:
            if len(var.workout_table) > 1:
                row, column = self.get_index_of_button(GUI.tableWidget_workout)
                if var.workout_table[row][5] == var.workout_table[row-1][5] and row != 0:
                    var.workout_table[row], var.workout_table[row-1] = var.workout_table[row-1], var.workout_table[row]
                    self.show_workout()
                else:
                    alert(text='Can\'t move', title='Alert', button='OK')
        except Exception as e:
            alert(text='Can\'t move', title='Alert', button='OK')
            print("Can't Move")

    def edit(self):
        row, column = self.get_index_of_button(GUI.tableWidget_workout)
        self.add_set()
        if column == 5:
            uw.main(row)
        else:
            uw.main(row)

        self.show_workout()

    def get_index_of_button(self, table):

        button = QtWidgets.qApp.focusWidget()
        # or button = self.sender()
        index = table.indexAt(button.pos())
        if index.isValid():
            # print(index.row(), index.column())
            return index.row(), index.column()

    def add_exercise(self):
        ae.main()
        self.show_exercises()


def add_muscle():
    am.main()
    Thread(target=show_muscle_groups, daemon=True).start()
    print("done")


def show_muscle_groups():
    try:
        con = db.DB()
        result = con.fetch_muscle_groups()
        result = list(result)
        print(result)
        var.muscle_groups = [] + result
        result.insert(0, "ALL")
        con.close()
        print(result)
        GUI.comboBox_exercise.clear()
        GUI.comboBox_exercise.addItems(result)

    except Exception as e:
        print("error at show_muscle_groups - {}".format(e))


def print_workout():
    try:
        var.printer_ip = GUI.lineEdit_ip.text()
        label_count = GUI.spinBox_print_labels.value()

        conn = db.DB()
        calories, exercise_time = list(), list()
        exercise_name = list()
        sets = list()
        types = list()
        workout_time = list()
        reps = list()
        rounds = list()
        for index, item in enumerate(var.workout_table):
            for index1, item1 in enumerate(var.workout_table):
                if var.workout_table[index][5] < var.workout_table[index1][5]:
                    var.workout_table[index], var.workout_table[index1] = var.workout_table[index1], var.workout_table[index]
        for item in var.workout_table:
            exercise_name.append(item[0])
            sets.append(item[5])
            types.append(item[1])
            workout_time.append(item[2])
            reps.append(item[3])
            rounds.append(item[4])
            temp, temp1 = conn.fetch_exercise_info2(item[0])
            calories.append(temp)
            exercise_time.append(temp1)
        conn.close()

        label = make_label(exercise_name, sets, types, calories,
                           exercise_time, workout_time, reps, rounds)
        for item in label.label().split("\n"):
            print(item)

        for index in range(label_count):
            # Printer IP Address
            printer = Network(var.printer_ip, profile="TM-T88V")
            printer.image("logo.png")
            for item in label.label().split("\n"):
                printer.text(item+"\n")
            printer.cut()
            printer.close()
    except Exception as e:
        print("Error at print_workout : {}".format(e))


class make_label():
    def __init__(self, exercise_name, sets, types, calories, exercise_time, workout_time, reps, rounds):
        self.exercise_name = exercise_name
        self.sets = sets
        self.types = types
        self.calories = calories
        self.exercise_time = exercise_time
        self.workout_time = workout_time
        self.reps = reps
        self.rounds = rounds

    def label(self):
        calories = 0
        try:
            for count in range(len(self.exercise_name)):
                if self.types[count] == "Time":
                    calories += (self.calories[count] * self.rounds[count] * (
                        self.workout_time[count]/self.exercise_time[count]))
                else:
                    calories += (self.calories[count] *
                                 self.rounds[count] * self.reps[count])
        except:
            pass

        time = 0
        for count in range(len(self.exercise_name)):
            if self.types[count] == "Reps":
                time += (self.reps[count] * self.rounds[count]
                         * self.exercise_time[count])
            else:
                time += (self.workout_time[count] * self.rounds[count])
        left = """\n\nCalories burned: {:.2f}\nEstimated workout time: {:.2f} min\n\nYou Can Do It!""".format(
            calories, time/60)

        right = """W O R K O U T   G E N E R A T O R\n\nDate:{}\n\n\n""".format(
            datetime.datetime.today().strftime('%d-%m-%Y'))
        if len(set(self.sets)) > 1:
            sets = list(set(self.sets))
            sets.sort()
            for index, item in enumerate(sets):
                right += str(item) + "\n\n"

                for name, v_type, time, reps, w_set, rounds in zip(self.exercise_name, self.types, self.workout_time, self.reps, self.sets, self.rounds):
                    if w_set == item:
                        right += name
                        if v_type == "Time":
                            right += "  {} seconds\n".format(
                                str(time)).rjust(40 - len(name))
                        elif v_type == "EMOM":
                            right += "  {} reps in {} seconds\n".format(
                                reps, time).rjust(40 - len(name))
                        else:
                            right += "  {} reps\n".format(
                                str(reps)).rjust(40 - len(name))
                        round = rounds
                right += "\nRepeat: " + str(round) + " rounds\n"
                if not index == len(sets)-1:
                    right += "________________________________\n\n"
        else:
            for name, v_type, time, reps, round in zip(self.exercise_name, self.types, self.workout_time, self.reps, self.rounds):
                right += name
                if v_type == "Time":
                    right += "  {} seconds {} rounds\n".format(
                        str(time), str(round)).rjust(40 - len(name))
                elif v_type == "EMOM":
                    right += "  {} reps in {} seconds {} rounds\n".format(
                        reps, time, round).rjust(40 - len(name))
                else:
                    right += "  {} reps {} rounds\n".format(
                        str(reps), str(round)).rjust(40 - len(name))

        return right + left


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    try:
        def resource_path(relative_path):
            if hasattr(sys, '_MEIPASS'):
                return os.path.join(sys._MEIPASS, relative_path)
            return os.path.join(os.path.abspath("."), relative_path)

        p = resource_path('icons/settings_applications-24px.svg')
        mainWindow.setWindowIcon(QtGui.QIcon(p))
    except Exception as e:
        print(e)

    mainWindow.setWindowFlags(mainWindow.windowFlags(
    ) | QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowSystemMenuHint)

    GUI = MyGui(mainWindow)
    # mainWindow.showMaximized()
    mainWindow.show()

    myMC = myMainClass()

    app.exec_()
    print("Exit")
    sys.exit()
