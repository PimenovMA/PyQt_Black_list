"""
:authors: Pimenov M.A. (Пименов Михаил Александрович)
:license: None License
Программа реализует функционал 'Черного списка' с использованием локальной базы данных
"""
import sqlite3
from PyQt5 import QtWidgets, QtCore
import sys

from PyQt5.QtWidgets import QTableWidgetItem


def button1_click():
    textedit1.setText(textline1.text())
    # запись данных в ячейку 0, 1
    tabedit1.setItem(0, 1, QTableWidgetItem (textline1.text()))
    # получение данных из ячейки 0, 1
    textline3.setText(tabedit1.item(0, 1).text())


def button2_click():
    textedit1.setText(textline2.text())
    tabedit1.setItem(0, 0, QTableWidgetItem ('Проверка'))

# БЛОК ПОСТРОЕНИЯ ГРАФИЧЕСКОГО ИНТЕРФЕЙСА

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle('Черный список клиентов')
# Фиксируем размер окна
window.setFixedSize(1000,700)

# Размещаем метку в позиции
label1 = QtWidgets.QLabel('Ф.И.О.:',window)
label1.setGeometry(10,5,100,20)

# Размещаем однострочное поле "Ф.И.О."
textline1 = QtWidgets.QLineEdit(window)
# устанвливаем размер поля
textline1.resize(250,20)
# размещаем поле в позиции
textline1.move(10,25)

# Размещаем метку в позиции
label2 = QtWidgets.QLabel('Адрес:',window)
label2.setGeometry(10,45,280,20)

# Размещаем однострочное поле "Адрес"
textline2 = QtWidgets.QLineEdit(window)
textline2.resize(250,20)
textline2.move(10,65)

# Размещаем метку в позиции
label3 = QtWidgets.QLabel('Телефон:',window)
label3.setGeometry(10,85,280,20)

# Размещаем однострочное поле "Телефон"
textline3 = QtWidgets.QLineEdit(window)
textline3.resize(250,20)
textline3.move(10,105)

# Размещаем метку в позиции
label4 = QtWidgets.QLabel('Паспорт серия номер:',window)
label4.setGeometry(10,125,280,20)

# Размещаем однострочное поле "Паспорт серия"
textline4 = QtWidgets.QLineEdit(window)
textline4.resize(250,20)
textline4.move(10,145)

# Размещаем метку в позиции
label5 = QtWidgets.QLabel('Дата выдачи:',window)
label5.setGeometry(10,165,280,20)

# Размещаем однострочное поле "Дата выдачи"
dateedit1 = QtWidgets.QDateEdit(window)
dateedit1.setCalendarPopup(True)
dateedit1.resize(250,20)
dateedit1.move(10,185)

# Размещаем метку в позиции
label6 = QtWidgets.QLabel('Кем выдан:',window)
label6.setGeometry(10,205,280,20)

# Размещаем однострочное поле "Кем выдан"
textline6 = QtWidgets.QLineEdit(window)
textline6.resize(250,20)
textline6.move(10,225)


# Размещаем метку в позиции
label7 = QtWidgets.QLabel('Код подразделения:',window)
label7.setGeometry(10,245,280,20)

# Размещаем однострочное поле "Код подразделения"
textline7 = QtWidgets.QLineEdit(window)
textline7.resize(250,20)
textline7.move(10,265)


# Размещаем метку в позиции
label8 = QtWidgets.QLabel('Претензия к клиенту:',window)
label8.setGeometry(10,285,280,20)

# Размещаем иногострочное поле "Претензия к клиенту"
textedit1 = QtWidgets.QTextEdit(window)
textedit1.setGeometry (10,305,250,330)

# Размещаем метку в позиции
label9 = QtWidgets.QLabel('Данные в БД:',window)
label9.setGeometry(280,5,280,20)

#Строим Таблицу и настраиваем ее параметры
tabedit1 = QtWidgets.QTableWidget(window)
tabedit1.setGeometry(280,25,700,610)
# задаем количество столбцов
tabedit1.setColumnCount(8)
# задаем название столбцов
tabedit1.setHorizontalHeaderLabels(["Ф.И.О.",
                                    "Адрес",
                                    "Телефон",
                                    "№ паспорта",
                                    "Дата выдачи",
                                    "Кем выдан",
                                    "Код подразделения",
                                    "Претензии"])
# задаем количество строк
tabedit1.setRowCount(5)
tabedit1.setVerticalHeaderLabels(['1','2','3','4','5'])
# разрешаем сортировку
tabedit1.setSortingEnabled(True)


# Размещаем кнопку "Поиск"
button1 =QtWidgets.QPushButton ('Поиск', window)
# устанавливаем размер кнопки
button1.resize(90,30)
# ставим ее в позицию
button1.move(10,650)

# Размещаем кнопку "Записать"
button2 =QtWidgets.QPushButton ('Записать', window)
button2.resize(90,30)
button2.move(110,650)

# Размещаем кнопку "Редактировать"
button3 =QtWidgets.QPushButton ('Редактировать', window)
button3.resize(90,30)
button3.move(210,650)

# КОНЕЦ БЛОКА ПОСТРОЕНИЯ ГРАФИЧЕСКОГО ИНТЕРФЕЙСА

button1.clicked.connect(button1_click)
button2.clicked.connect(button2_click)
window.show()
sys.exit(app.exec_())
