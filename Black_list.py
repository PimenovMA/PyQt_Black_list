"""
:authors: Pimenov M.A. (Пименов Михаил Александрович)
:license: None License

"""
import sqlite3
from PyQt5 import QtWidgets, QtCore
import sys

# БЛОК ПОСТРОЕНИЯ ГРАФИЧЕСКОГО ИНТЕРФЕЙСА

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle('Черный список клиентов')
# Фиксируем размер окна
window.setFixedSize(900,700)

# Размещаем метку в позиции
label1 = QtWidgets.QLabel('Фамилия:',window)
label1.setGeometry(10,5,280,60)

# Размещаем однострочное поле "Фамилия"
textline1 = QtWidgets.QLineEdit(window)
# устанвливаем размер поля
textline1.resize(200,20)
# размещаем поле в позиции
textline1.move(10,45)

# Размещаем метку в позиции
label2 = QtWidgets.QLabel('Имя:',window)
label2.setGeometry(10,45,280,60)

# Размещаем однострочное поле "Имя"
textline2 = QtWidgets.QLineEdit(window)
textline2.resize(200,20)
textline2.move(10,85)

# Размещаем метку в позиции
label3 = QtWidgets.QLabel('Отчество:',window)
label3.setGeometry(10,85,280,60)

# Размещаем однострочное поле "Отчество"
textline3 = QtWidgets.QLineEdit(window)
textline3.resize(200,20)
textline3.move(10,125)

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
button2 =QtWidgets.QPushButton ('Редактировать', window)
button2.resize(90,30)
button2.move(210,650)


window.show()

sys.exit(app.exec_())
