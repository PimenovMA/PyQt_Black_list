from PyQt5.QtWidgets import *
from PyQt5.QtGui import QKeySequence

class MainWindow(QMainWindow):
    def closeEvent(self, e):
        if not text.document().isModified():
            return
        answer = QMessageBox.question(
            window, None,
            "You have unsaved changes. Save before closing?",
            QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel
        )
        if answer & QMessageBox.Save:
            save()
        elif answer & QMessageBox.Cancel:
            e.ignore()

app = QApplication([])
app.setApplicationName("Текстовый редактор")
text = QPlainTextEdit()
window = MainWindow()
window.setCentralWidget(text)

file_path = None

menu = window.menuBar().addMenu("&Файл")
open_action = QAction("&Открыть")
def open_file():
    global file_path
    path = QFileDialog.getOpenFileName(window, "Сохранение")[0]
    if path:
        text.setPlainText(open(path).read())
        file_path = path
open_action.triggered.connect(open_file)
open_action.setShortcut(QKeySequence.Open)
menu.addAction(open_action)

save_action = QAction("&Сохранить")
def save():
    if file_path is None:
        save_as()
    else:
        with open(file_path, "w") as f:
            f.write(text.toPlainText())
        text.document().setModified(False)
save_action.triggered.connect(save)
save_action.setShortcut(QKeySequence.Save)
menu.addAction(save_action)

save_as_action = QAction("Сохранить &как...")
def save_as():
    global file_path
    path = QFileDialog.getSaveFileName(window, "Сохранить как")[0]
    if path:
        file_path = path
        save()
save_as_action.triggered.connect(save_as)
menu.addAction(save_as_action)

close = QAction("&Закрыть")
close.triggered.connect(window.close)
menu.addAction(close)

help_menu = window.menuBar().addMenu("&Помощь")
about_action = QAction("&О программе")
help_menu.addAction(about_action)
def show_about_dialog():
    text = "<center>" \
           "<h1>Текстовый редактор</h1>" \
           "&#8291;" \
           "<img src=icon.svg>" \
           "</center>" \
           "<p>Версия 31.4.159.265358<br/>" \
           "Все права защищены.</p>"
    QMessageBox.about(window, "О редакторе", text)
about_action.triggered.connect(show_about_dialog)

window.show()
app.exec_()