from PyQt5 import QtWidgets, QtCore
import sys


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
        self.found_button.clicked.connect(self.delete_clicked)

        self.tablist = QtWidgets.QTableWidget(self)
        self.tablist.setGeometry (300,10,500,100)
        self.tablist.setColumnCount(3)
        self.tablist.setSortingEnabled(True)
        self.column_label = ['ID','Ф.И.О','Серия и N паспорта']
        self.tablist.setHorizontalHeaderLabels(self.column_label)
        self.tablist.resizeColumnToContents(0)
        self.tablist.resizeColumnToContents(1)
        self.tablist.resizeColumnToContents(2)
        self.tablist.insertRow(self.tablist.rowCount())

    def found_clicked(self):
        pass

    def delete_clicked(self):
        pass

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    form1 = Window_one()
    form1.setFixedSize(810,130)
    form1.setWindowModality(1)
    form1.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
    form1.setWindowTitle('Удаление записи')
    form1.show()
    sys.exit (app.exec_())
