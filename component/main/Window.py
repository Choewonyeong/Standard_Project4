from PyQt5.QtWidgets import *
from component.widget.CheckBoxTask import CheckBoxTask


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.__setting__()
        self.__component__()
        self.__variables__()

    def __setting__(self):
        pass

    def __component__(self):
        self.cbxTask = CheckBoxTask()
        self.__layout__()

    def __variables__(self):
        self.task = self.cbxTask.taskList

    def __layout__(self):
        layout = QVBoxLayout()
        layout.addWidget(self.cbxTask)
        self.setLayout(layout)

