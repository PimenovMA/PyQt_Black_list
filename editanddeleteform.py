from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5 import QtWidgets, QtCore
import sys, peewee

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

class Window_one (QtWidgets.QWidget):
    def __init__(self):
        super(Window_one, self).__init__()

        self.label1 = QtWidgets.QLabel ('Кого ищем?', self)
        self.label1.setGeometry(10,10,70,20)

        self.foundtext_line = QtWidgets.QLineEdit (self)
        self.foundtext_line.resize(280,25)
        self.foundtext_line.move(10,30)

        self.found_button = QtWidgets.QPushButton('Поиск ', self)
        self.found_button.resize(100,30)
        self.found_button.move(40,70)
        self.found_button.clicked.connect(self.found_clicked)

        self.delete_button = QtWidgets.QPushButton('Удаление', self)
        self.delete_button.resize(100,30)
        self.delete_button.move(170,70)
        self.delete_button.clicked.connect(self.delete_clicked)

        self.tablist = QtWidgets.QTableWidget(self)
        self.tablist.setGeometry (300,10,500,100)
        self.tablist.setColumnCount(3)
        self.tablist.setRowCount(1)
        self.tablist.setSortingEnabled(True)
        self.column_label = ['ID','Ф.И.О','Серия и N паспорта']
        self.tablist.setHorizontalHeaderLabels(self.column_label)
        self.tablist.resizeColumnToContents(0)
        self.tablist.resizeColumnToContents(1)
        self.tablist.resizeColumnToContents(2)

    def delete_clicked(self):
        """
        Удаление записи из БД по ID
        """

        #self.tablist.setItem(0, 1, QTableWidgetItem("Первая вставка"))
        self.tablist.setItem(0, 1, QTableWidgetItem(self.foundtext_line.text().upper()))
        self.tablist.insertRow(self.tablist.rowCount())

    def found_clicked(self):
        """
        Поиск записи в БД и вывод списка найденного в таблицу с привязкой ID
        """

        self.tablist.clearContents()
        row_count = 0
        quere = Person.select().where((Person.name.contains('%' + self.foundtext_line.text().upper() + '%')))
        for data in quere:  # Заполняем таблицу полученными данными
            self.tablist.setItem(row_count, 0, QTableWidgetItem(str(data.id)))
            self.tablist.setItem(row_count, 1, QTableWidgetItem(data.name))
            self.tablist.setItem(row_count, 2, QTableWidgetItem(data.passport))
            row_count += 1
            self.tablist.insertRow(self.tablist.rowCount())  # Добавляем в таблицу пустую строчку
        self.foundtext_line.clear()
        self.tablist.resizeColumnToContents(0)
        self.tablist.resizeColumnToContents(1)
        self.tablist.resizeColumnToContents(2)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    form1 = Window_one()
    form1.setFixedSize(810,130)
    #form1.setWindowModality(1)
    form1.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
    form1.setWindowTitle('Удаление записи')
    form1.show()
    sys.exit (app.exec_())
