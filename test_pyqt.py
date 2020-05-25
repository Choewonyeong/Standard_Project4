from component.main.Window import Window
from sys import argv
from PyQt5.QtWidgets import QApplication


if __name__ == "__main__":
    app = QApplication(argv)
    win = Window()
    win.show()
    app.exec_()