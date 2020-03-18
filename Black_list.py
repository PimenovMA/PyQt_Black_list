# -*- coding: utf-8 -*-

"""
:authors: Pimenov M.A. (Пименов Михаил Александрович)
:license: None License
Программа реализует функционал 'Черного списка' с использованием локальной базы данных
"""
import peewee
from datetime import date
from PyQt5 import QtWidgets
import sys
from PyQt5.QtWidgets import QTableWidgetItem, QCalendarWidget

table_count = 0 # Счетчик строчек таблицы (глобальная переменная)
# БЛОК РАБОТЫ С БАЗОЙ ДАННЫХ

database = peewee.SqliteDatabase ('blacklist.db')

class Person (peewee.Model):
    name = peewee.CharField(50)
    adress = peewee.CharField(80)
    telephone = peewee.CharField(15)
    passport = peewee.CharField(13)
    date_out = peewee.DateField()
    out_passport = peewee.CharField()
    id_passport = peewee.CharField()
    bad_human = peewee.CharField(50)
    date_add = peewee.DateField()
    class Meta:
        database = database


def button1_click():
    """Очистка Таблицы виджета, Текстовых полей, обнуление счетчика строк таблицы виджета"""
    global table_count
    table_count = 0 # обнуляем счетчик строк таблыцы виджета
    tabedit1.setRowCount(1) # сбрасываем строки к дефолту
    tabedit1.clearContents() # очистка данных в ячейках таблицы
    # Очищаем текстовые поля
    textline1.clear(); textline2.clear(); textline3.clear(); textline4.clear(); textline6.clear(); textline7.clear()
    textedit1.clear()


def button2_click(): # Запись введенных данных в БД
    database.create_tables([Person]) # создаем БД и таблицу Person. Если есть, открываем на редактирование.
    record_db = Person(name = textline1.text(),
                       adress = textline2.text(),
                       telephone = textline3.text(),
                       passport = textline4.text(),
                       date_out = dateedit1.dateTime().toString('dd-MM-yyyy'),
                       out_passport = textline6.text(),
                       id_passport = textline7.text(),
                       bad_human = textedit1.toPlainText(),
                       date_add = date.today())
    record_db.save()
    global table_count
    # Заполняем таблицу введенными данными
    tabedit1.setItem(table_count, 0, QTableWidgetItem (textline1.text()))
    tabedit1.setItem(table_count, 1, QTableWidgetItem (textline2.text()))
    tabedit1.setItem(table_count, 2, QTableWidgetItem (textline3.text()))
    tabedit1.setItem(table_count, 3, QTableWidgetItem (textline4.text()))
    tabedit1.setItem(table_count, 4, QTableWidgetItem (dateedit1.dateTime().toString('dd-MM-yyyy')))
    tabedit1.setItem(table_count, 5, QTableWidgetItem (textline6.text()))
    tabedit1.setItem(table_count, 6, QTableWidgetItem (textline7.text()))
    tabedit1.setItem(table_count, 7, QTableWidgetItem (textedit1.toPlainText()))
    # Очищаем текстовые поля
    textline1.clear(); textline2.clear(); textline3.clear(); textline4.clear(); textline6.clear(); textline7.clear()
    textedit1.clear()
    table_count += 1 # Увеличиваем счетчик строк в таблице
    tabedit1.insertRow(tabedit1.rowCount()) # Добавляем в таблицу пустую строчку

def button3_click():
    textline1.setText(textline3.text())


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
textline3.setInputMask("+7 999-999-99-99;_")
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
tabedit1.setRowCount(1)
tabedit1.setVerticalHeaderLabels(['1','2','3','4','5'])
# разрешаем сортировку
tabedit1.setSortingEnabled(True)


# Размещаем кнопку "Поиск"
button1 =QtWidgets.QPushButton ('Очистить', window)
# устанавливаем размер кнопки
button1.resize(90,30)
# ставим ее в позицию
button1.move(10,650)

# Размещаем кнопку "Записать"
button2 =QtWidgets.QPushButton ('Записать', window)
button2.resize(90,30)
button2.move(110,650)

# Размещаем кнопку "Редактировать"
button3 =QtWidgets.QPushButton ('Тестовая', window)
button3.resize(90,30)
button3.move(210,650)

# КОНЕЦ БЛОКА ПОСТРОЕНИЯ ГРАФИЧЕСКОГО ИНТЕРФЕЙСА

button1.clicked.connect(button1_click)
button2.clicked.connect(button2_click)
button3.clicked.connect(button3_click)
window.show()
sys.exit(app.exec_())
