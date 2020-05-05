import sys
from PyQt5 import QtCore, QtWidgets

class Formedit (QtWidgets.QWidget):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        self.label1 = QtWidgets.QLabel('Привет всем!', self)
        self.label1.setGeometry(10,5,100,20)
        self.button1 = QtWidgets.QPushButton('Кнопка', self)
        self.button1.resize(90,30)
        self.button1.move(10,650)
        self.button1.clicked.connect(self.on_clicked)
    def on_clicked(self):
        self.label1.setText('ЭТО НОВЫЙ ТЕКСТ')
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    wind = Formedit()
    wind.setFixedSize(1000,700)
    wind.show()
    sys.exit(app.exec_())