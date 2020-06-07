import sys, peewee
from datetime import date
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

class Editform(QtWidgets.QWidget):
    def __init__(self):
        super(Editform, self).__init__()
        self.setWindowTitle('Window2')
        """
    def __init__(self, parent = None):
        self.label1 = QtWidgets.QLabel('ПРИВЕТ мир')
        self.button1 = QtWidgets.QPushButton('Кнопка')
        self.button1.clicked.connect(self.on_clicked)
    def on_clicked(self):
        pass
        """