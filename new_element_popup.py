from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Type_element(QComboBox):
    def __init__(self):
        super().__init__()
        self.elements = ['', 'Кнопка', 'Секция шин']
        self.addItems(self.elements)


class AnotherWindow(QDialog):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
        self.labels = ["Тип элемента", "Привязка к модулю", "Имя элемента"]
        self.main = root

        self.setFixedHeight(200)
        self.setFixedWidth(500)

        main_layout = QVBoxLayout()

        top_layout = QHBoxLayout()
        middle_layout_1 = QHBoxLayout()
        middle_layout_2 = QHBoxLayout()
        bottom_layout = QHBoxLayout()

        self.label_top = QLabel("Тип элемента")

        self.cb_top = Type_element()
        self.cb_top.setFixedWidth(self.width() - len(max(self.labels, key=len)) - 150)

        self.label_middle = QLabel("Привязка к модулю")

        self.cb_middle = QComboBox()
        self.cb_middle.setFixedWidth(self.width() - len(max(self.labels, key=len)) - 150)

        self.label_bottom = QLabel("Имя элемента")

        self.le = QLineEdit()
        self.le.setFixedWidth(self.width() - len(max(self.labels, key=len)) - 150)

        bt_ok = QPushButton('Применить')
        bt_cancel = QPushButton('Отмена')
        bt_cancel.pressed.connect(self.close)
        bt_ok.pressed.connect(self.apply)

        top_layout.addWidget(self.label_top)
        top_layout.addWidget(self.cb_top)

        middle_layout_1.addWidget(self.label_middle)
        middle_layout_1.addWidget(self.cb_middle)

        middle_layout_2.addWidget(self.label_bottom)
        middle_layout_2.addWidget(self.le)

        bottom_layout.addWidget(bt_ok)
        bottom_layout.addWidget(bt_cancel)

        main_layout.addLayout(top_layout)
        main_layout.addLayout(middle_layout_1)
        main_layout.addLayout(middle_layout_2)
        main_layout.addLayout(bottom_layout, Qt.AlignRight)

        self.setLayout(main_layout)

    def apply(self):
        self.main.update([self.cb_top.currentText(), self.cb_middle.currentText(), self.le.text()])
        self.close()