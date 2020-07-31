from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5 import QtWidgets, QtCore
import sys, peewee

database = peewee.SqliteDatabase('blacklist.db')


class Person (peewee.Model):
    name = peewee.CharField(50)        # ФИО клиента
    adress = peewee.CharField(80)      # адрес клиента
    telephone = peewee.CharField(15)   # телефон клиента
    passport = peewee.CharField(13)    # номер и серия паспорта
    date_out = peewee.DateField()      # дата выдачи
    out_passport = peewee.CharField()  # кем выдан
    id_passport = peewee.CharField()   # код подразделения
    bad_human = peewee.CharField(50)   # косяки клиента
    date_add = peewee.DateField()

    class Meta:
        database = database


class Window_one (QtWidgets.QWidget):
    def __init__(self):
        super(Window_one, self).__init__()

        self.label1 = QtWidgets.QLabel('Кого ищем?', self)
        self.label1.setGeometry(10, 10, 70, 20)

        self.foundtext_line = QtWidgets.QLineEdit(self)
        self.foundtext_line.resize(280, 25)
        self.foundtext_line.move(10, 30)

        self.found_button = QtWidgets.QPushButton('Поиск ', self)
        self.found_button.resize(100, 30)
        self.found_button.move(40, 70)
        self.found_button.clicked.connect(self.found_clicked)

        self.delete_button = QtWidgets.QPushButton('Удаление', self)
        self.delete_button.resize(100, 30)
        self.delete_button.move(170, 70)
        self.delete_button.setEnabled(False)
        self.delete_button.clicked.connect(self.delete_clicked)

        self.tablist = QtWidgets.QTableWidget(self)
        self.tablist.setGeometry(300, 10, 500, 100)
        self.tablist.setColumnCount(3)
        self.tablist.setRowCount(1)
        self.tablist.setSortingEnabled(True)
        self.tablist.setHorizontalHeaderLabels(['ID', 'Ф.И.О', 'Серия и N паспорта'])
        self.tablist.resizeColumnToContents(0)
        self.tablist.resizeColumnToContents(1)
        self.tablist.resizeColumnToContents(2)

    def delete_clicked(self):
        """
        Удаление записи из БД по ID
        """
        self.foundtext_line.setText(self.tablist.item(self.tablist.currentRow(), 0).text())
        # получение значения ячейки из таблицы
        self.tablist.insertRow(self.tablist.rowCount())
        self.delete_button.setEnabled(False)

    def found_clicked(self):
        """
        Поиск записи в БД и вывод списка найденного в таблицу с привязкой ID
        """
        if self.foundtext_line.text() != "":
            self.tablist.clearContents()
            row_count1 = 0  # Счетчик строк
            quere = Person.select().where((Person.name.contains('%' + self.foundtext_line.text().upper() + '%')))
            for data in quere:  # Заполняем таблицу полученными данными
                self.tablist.setItem(row_count1, 0, QTableWidgetItem(str(data.id)))
                self.tablist.setItem(row_count1, 1, QTableWidgetItem(data.name))
                self.tablist.setItem(row_count1, 2, QTableWidgetItem(data.passport))
                row_count1 += 1
                self.tablist.insertRow(self.tablist.rowCount())  # Добавляем в таблицу пустую строчку
            self.foundtext_line.clear()
            self.delete_button.setEnabled(True)
            self.tablist.resizeColumnToContents(0)
            self.tablist.resizeColumnToContents(1)
            self.tablist.resizeColumnToContents(2)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    form1 = Window_one()
    form1.setFixedSize(810, 130)
    # form1.setWindowModality(1)
    form1.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
    form1.setWindowTitle('Удаление записи')
    form1.show()
    sys.exit(app.exec_())
