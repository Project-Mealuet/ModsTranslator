from PyQt6.QtWidgets import QApplication, QMainWindow
from sys import argv, exit
from functions.jarClass import jarTranslation


if __name__ == '__main__':
    app = QApplication(argv)
    mainWindow = QMainWindow()
    UI = jarTranslation(mainWindow)
    mainWindow.show()
    exit(app.exec())
