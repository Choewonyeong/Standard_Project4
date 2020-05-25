from PyQt5.QtWidgets import *


class CheckBoxTask(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.taskList = []
        self.__variables__()
        self.__component__()

    def __variables__(self):
        self.titles = ['전체', '물품', '공사', '용역', '리스', '외자', '비축', '기타', '민간']
        self.element = ['taskClCds', 'taskClCds1', 'taskClCds3', 'taskClCds5', 'taskClCds6',
                        'taskClCds2', 'taskClCds11', 'taskClCds4', 'taskClCds20']

    def __component__(self):
        self.__comboBox__()
        self.__layout__()

    def __comboBox__(self):
        def objComboBoxClick(value):
            widget = self.sender()
            idx = self.titles.index(widget.text())
            if value:
                self.taskList.append(self.element[idx])
            elif not value:
                self.taskList.remove(widget.text())
        self.objects = []
        for title in self.titles:
            obj = QCheckBox(title)
            obj.clicked.connect(objComboBoxClick)
            self.objects.append(obj)

    def __layout__(self):
        layout = QHBoxLayout()
        for obj in self.objects:
            layout.addWidget(obj)
        self.setLayout(layout)

