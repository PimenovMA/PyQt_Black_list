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
        self.found_button.clicked.connect(found_clicked)

        self.delete_button = QtWidgets.QPushButton('Удаление', self)
        self.delete_button.resize(100,30)
        self.delete_button.move(170,70)
        self.found_button.clicked.connect(delete_clicked)

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


def delete_clicked():
    form1.tablist.setItem (1, 1, form1.tablist.QTableWidgetItem(form1.foundtext_line.text().upper()))

def found_clicked():
    form1.tablist.clearContents()
    row_count = 0
    quere1 = Person.select().where((Person.name.contains('%'+form1.foundtext_line.text().upper()+'%')))
    for data in quere1: # Заполняем таблицу полученными данными
        #self.tablist.setItem (row_count, 0, self.QTableWidgetItem (self.data.id))
        form1.tablist.setItem (row_count, 1, form1.tablist.QTableWidgetItem (data.name))
        form1.tablist.setItem (row_count, 2, form1.tablist.QTableWidgetItem (data.passport))
        row_count += 1
        form1.tablist.insertRow(form1.tablist.rowCount()) # Добавляем в таблицу пустую строчку
    form1.foundtext_line.clear()
    form1.tablist.resizeColumnToContents(0)
    form1.tablist.resizeColumnToContents(1)
    form1.tablist.resizeColumnToContents(2)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    form1 = Window_one()
    form1.setFixedSize(810,130)
    #form1.setWindowModality(1)
    form1.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
    form1.setWindowTitle('Удаление записи')
    form1.foundtext_line.setText('ПИМЕНОВ')
    form1.show()
    sys.exit (app.exec_())
