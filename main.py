from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore
import sys

import GroupButton
import new_element_popup as new


class Main(QMainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.current_choice = []
        self.w = None
        self.pos_x = 0
        self.pos_y = 0
        self.nm = ''
        self.setWindowTitle('Imit')
        self.setGeometry(250, 200, 1300, 700)
        self.setMinimumSize(1300, 700)
        self._createActions()
        self._createMenuBar()

        layout_left = QVBoxLayout()
        layout_right = QHBoxLayout()
        layout_central = QHBoxLayout()

        self.gr = QGroupBox('Control window')
        self.gr.setFixedHeight(130)
        self.bt = GroupButton.GroupButton(3, ['Open', 'Close', 'Stop']).add()
        self.gr.setLayout(self.bt)
        layout_left.addWidget(self.gr)

        tab1 = QTableWidget()
        layout_left.addWidget(tab1, QtCore.Qt.AlignTop)
        tab2 = QTableWidget()
        tab2.setFixedHeight(200)
        layout_left.addWidget(tab2, QtCore.Qt.AlignTop)

        self.scr_area = QScrollArea()
        self.group_element = QWidget()
        self.scr_area.setWidget(self.group_element)
        self.scr_area.setWidgetResizable(True)
        self.group_element_layout = QGridLayout(self.group_element)
        self.group_element_layout.setSpacing(5)
        self.group_element_layout.setSizeConstraint(QLayout.SetFixedSize)
        # scr_area.setGeometry(0, 0, 500, 699)

        layout_right.addWidget(self.scr_area)
        # layout_right.addStretch(1)

        layout_central.addLayout(layout_left)
        layout_central.addLayout(layout_right)

        main_widget = QWidget()
        main_widget.setLayout(layout_central)
        self.setCentralWidget(main_widget)

    def _createMenuBar(self):
        self.menu_Bar = self.menuBar()
        self.file_Menu = QMenu("Настройки", self)
        self.menu_Bar.addMenu(self.file_Menu)
        # self.newAction = QAction("Добавить", self)
        self.file_Menu.addAction(self.newAction)
        self.file_Menu.addAction(self.delete_one)
        self.file_Menu.addAction(self.delete_all)

    def _createActions(self):
        self.newAction = QAction("Добавить элемент", self)
        self.newAction.triggered.connect(self.add_element)
        self.delete_one = QAction("Удалить элемент", self)
        self.delete_one.triggered.connect(self.del_element)
        self.delete_all = QAction("Удалить все элементы", self)
        self.delete_all.triggered.connect(self.del_all_elements)

    def add_element(self, checked):
        self.w = new.AnotherWindow(self)
        self.w.show()

    def update(self, *args):
        if args[0] in self.current_choice:
            pass
        else:
            self.current_choice.append(*args)
            self.gr.setTitle(args[0][2])
            self.add_form(*args)

    def add_form(self, *args):
        self.bt = QPushButton(args[0][2])
        self.nm = args[0][2]
        self.bt.pressed.connect(lambda numButton=args[0][2]: self.update_controk_window(numButton))
        self.bt.setFixedHeight(100)
        self.bt.setFixedWidth(100)
        if self.pos_y < 6:
            self.group_element_layout.addWidget(self.bt, self.pos_x, self.pos_y)
            self.pos_y += 1
        else:
            self.pos_x += 1
            self.pos_y = 0
            self.group_element_layout.addWidget(self.bt, self.pos_x, self.pos_y)
            self.pos_y += 1

    def del_element(self):
        for i in reversed(range(self.group_element_layout.count())):
            if self.group_element_layout.itemAt(i).widget().text() == self.nm:
                self.group_element_layout.itemAt(i).widget().setParent(None)

    def del_all_elements(self):
        for i in reversed(range(self.group_element_layout.count())):
            if self.group_element_layout.itemAt(i).widget():
                self.group_element_layout.itemAt(i).widget().setParent(None)
            else:
                self.group_element_layout.removeItem(self.group_element_layout.itemAt(i))

    def update_controk_window(self, numButton):
        self.nm = numButton
        self.gr.setTitle(self.nm)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWidget = Main()
    myWidget.show()
    sys.exit(app.exec_())
