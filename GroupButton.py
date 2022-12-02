from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton


class GroupButton(QWidget):
    def __init__(self, count_bt=1, name=[]):
        super().__init__()
        self.name = name
        self.count_bt = count_bt
        self.hbox = QHBoxLayout()

    def add(self):
        for i in range(self.count_bt):
            if not self.name:
                bt = QPushButton('Btn' + str(i))
            else:
                bt = QPushButton(self.name[i])
            bt.setFixedWidth(70)
            bt.setFixedHeight(70)
            bt.setStyleSheet("""
                                background-color: rgb(61, 92, 244);
                                color: rgb(255,255,255);  
                                border-radius: 35px;  border: 2px groove gray;
                                font: 9pt "AcadEref";
                                border-style: outset;
            """
            )
            self.hbox.addWidget(bt)
        return self.hbox