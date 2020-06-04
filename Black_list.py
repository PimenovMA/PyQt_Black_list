#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:authors: Pimenov M.A. (Пименов Михаил Александрович)
:license: None License
Программа реализует функционал 'Черного списка' с использованием локальной базы данных SQLite
"""
import sys, peewee
from datetime import date
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

row_count = 0 # Счетчик строчек таблицы (глобальная переменная)

# БЛОК РАБОТЫ С БАЗОЙ ДАННЫХ
database = peewee.SqliteDatabase ('blacklist.db')

class Person (peewee.Model):
    name = peewee.CharField(50) # ФИО клиента  textline1
    adress = peewee.CharField(80) # адрес клиента textline2
    telephone = peewee.CharField(15) # телефон клиента textline3
    passport = peewee.CharField(13) # номер и серия паспорта textline4
    date_out = peewee.DateField() # дата выдачи dateedit1
    out_passport = peewee.CharField() # кем выдан textline6
    id_passport = peewee.CharField() # код подразделения textline7
    bad_human = peewee.CharField(50) # косяки клиента textedit1
    date_add = peewee.DateField()
    class Meta:
        database = database


def button1_click():
    """Очистка Таблицы виджета, Текстовых полей, обнуление счетчика строк таблицы виджета"""
    global row_count
    row_count = 0 # обнуляем счетчик строк таблицы виджета
    tabedit1.setRowCount(1) # сбрасываем строки к дефолту
    tabedit1.clearContents() # очистка данных в ячейках таблицы
    # Очищаем текстовые поля
    textline1.clear(); textline2.clear(); textline3.clear(); textline4.clear(); textline6.clear(); textline7.clear()
    textedit1.clear()


def button2_click(): # Запись введенных данных в БД
    database.create_tables([Person]) # создаем БД и таблицу Person. Если есть, открываем на редактирование.
    record_db = Person(name = textline1.text().upper(),
                       adress = textline2.text().upper(),
                       telephone = textline3.text().upper(),
                       passport = textline4.text().upper(),
                       date_out = dateedit1.dateTime().toString('dd-MM-yyyy'),
                       out_passport = textline6.text().upper(),
                       id_passport = textline7.text().upper(),
                       bad_human = textedit1.toPlainText(),
                       date_add = date.today())
    record_db.save()
    global row_count
    # Заполняем таблицу введенными данными
    tabedit1.setItem(row_count, 0, QTableWidgetItem (textline1.text().upper()))
    tabedit1.setItem(row_count, 1, QTableWidgetItem (textline2.text().upper()))
    tabedit1.setItem(row_count, 2, QTableWidgetItem (textline3.text().upper()))
    tabedit1.setItem(row_count, 3, QTableWidgetItem (textline4.text()))
    tabedit1.setItem(row_count, 4, QTableWidgetItem (dateedit1.dateTime().toString('dd-MM-yyyy')))
    tabedit1.setItem(row_count, 5, QTableWidgetItem (textline6.text().upper()))
    tabedit1.setItem(row_count, 6, QTableWidgetItem (textline7.text()))
    tabedit1.setItem(row_count, 7, QTableWidgetItem (textedit1.toPlainText()))
    tabedit1.resizeColumnToContents(0) # автоподбор ширины столбца Ф.И.О.
    # Очищаем текстовые поля
    textline1.clear(); textline2.clear(); textline3.clear(); textline4.clear(); textline6.clear(); textline7.clear()
    textedit1.clear()
    row_count += 1
    tabedit1.insertRow(tabedit1.rowCount()) # Добавляем в таблицу пустую строчку

def button3_click():
    # Функция Удаления/Редактирования записей в БД
    # проба запуска2

    pass

def next_focus(): textline2.setFocus()
def next_focus1(): textline3.setFocus()
def next_focus2(): textline4.setFocus()
def next_focus3(): dateedit1.setFocus()
def next_focus4(): textline7.setFocus()
def next_focus5(): textedit1.setFocus()

def button_find():
    # Поиск в Базе Данных
    tabedit1.clearContents()
    global row_count
    row_count = 0
    quere = Person.select().where((Person.name.contains('%'+textline1.text().upper()+'%')))
    for data in quere: # Заполняем таблицу полученными данными
        tabedit1.setItem (row_count, 0, QTableWidgetItem (data.name))
        tabedit1.setItem (row_count, 1, QTableWidgetItem (data.adress))
        tabedit1.setItem (row_count, 2, QTableWidgetItem (data.telephone))
        tabedit1.setItem (row_count, 3, QTableWidgetItem (data.passport))
        tabedit1.setItem (row_count, 4, QTableWidgetItem (data.date_out))
        tabedit1.setItem (row_count, 5, QTableWidgetItem (data.out_passport))
        tabedit1.setItem (row_count, 6, QTableWidgetItem (data.id_passport))
        tabedit1.setItem (row_count, 7, QTableWidgetItem (data.bad_human))
        row_count += 1
        tabedit1.insertRow(tabedit1.rowCount()) # Добавляем в таблицу пустую строчку
        textline1.clear()
    tabedit1.resizeColumnToContents(0)


def button_view():
    # Просмотр ВСЕЙ информации введенной в БД
    global row_count
    row_count = 0 # счетчик строк в таблице
    quere = Person.select()
    for data in quere: # Заполняем таблицу полученными данными
        tabedit1.setItem (row_count, 0, QTableWidgetItem (data.name))
        tabedit1.setItem (row_count, 1, QTableWidgetItem (data.adress))
        tabedit1.setItem (row_count, 2, QTableWidgetItem (data.telephone))
        tabedit1.setItem (row_count, 3, QTableWidgetItem (data.passport))
        tabedit1.setItem (row_count, 4, QTableWidgetItem (data.date_out))
        tabedit1.setItem (row_count, 5, QTableWidgetItem (data.out_passport))
        tabedit1.setItem (row_count, 6, QTableWidgetItem (data.id_passport))
        tabedit1.setItem (row_count, 7, QTableWidgetItem (data.bad_human))
        row_count += 1
        tabedit1.insertRow(tabedit1.rowCount()) # Добавляем в таблицу пустую строчку
    tabedit1.resizeColumnToContents(0)



# БЛОК ПОСТРОЕНИЯ ГРАФИЧЕСКОГО ИНТЕРФЕЙСА

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle('Черный список клиентов')
# Фиксируем размер окна
window.setFixedSize(1000,700)

# Размещаем метку в позиции
label1 = QtWidgets.QLabel('Ф.И.О.:', window)
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
textline4.setInputMask("99 99 999999; ")
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
textline7.setInputMask("999-999; ")
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
button1.resize(100,30) # устанавливаем размер кнопки
button1.move(10,650) # ставим ее в позицию

# Размещаем кнопку "Записать"
button2 = QtWidgets.QPushButton ('Записать', window)
button2.resize(100,30)
button2.move(110,650)

# Размещаем кнопку "Редактировать"
button3 = QtWidgets.QPushButton ('Изменить в БД', window)
button3.resize(100,30)
button3.move(210,650)

# Размещаем кнопку "Поиск"
button_find1 = QtWidgets.QPushButton ('Поиск в БД', window)
button_find1.resize(100,30)
button_find1.move(310,650)

# Размещаем кнопку "Посмотреть БД"
button_view1 = QtWidgets.QPushButton ('Просмотр БД', window)
button_view1.resize(100,30)
button_view1.move(410,650)

# КОНЕЦ БЛОКА ПОСТРОЕНИЯ ГРАФИЧЕСКОГО ИНТЕРФЕЙСА

# БЛОК УПРАВЛЕНИЕМ ФОКУСОМ ЭЛЕМЕНТОВ ИНТЕРФЕЙСА
textline1.returnPressed.connect(next_focus)
textline2.returnPressed.connect(next_focus1)
textline3.returnPressed.connect(next_focus2)
textline4.returnPressed.connect(next_focus3)
textline6.returnPressed.connect(next_focus4)
textline7.returnPressed.connect(next_focus5)
# КОНЕЦ БЛОКА УПРАВЛЕНИЕМ ФОКУСОМ ЭЛЕМЕНТОВ ИНТЕРФЕЙСА

# БЛОК УПРАВЛЕНИЯ КНОПКАМИ
button1.clicked.connect(button1_click)
button2.clicked.connect(button2_click)
button3.clicked.connect(button3_click)
button_find1.clicked.connect(button_find)
button_view1.clicked.connect(button_view)
# КОНЕЦ БЛОКА УПРАВЛЕНИЯ КНОПКАМИ

window.show()
sys.exit(app.exec_())
