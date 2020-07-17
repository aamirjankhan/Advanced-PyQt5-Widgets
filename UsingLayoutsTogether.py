import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Horizontal And Vertical Layouts")
        self.setGeometry(500 , 250 , 400 , 400)
        self.UI()
    def UI(self):
        MainLayout=QVBoxLayout()
        TopLayout=QHBoxLayout()
        BottomLayout=QHBoxLayout()
        cbox=QCheckBox()
        rbtn=QRadioButton()
        combo=QComboBox()
        btn1=QPushButton()
        btn2=QPushButton()
        TopLayout.addWidget(cbox)
        TopLayout.setContentsMargins(150,10,20,20) #left, top, right, bottom
        BottomLayout.setContentsMargins(150,10,150,10)
        TopLayout.addWidget(rbtn)
        TopLayout.addWidget(combo)
        BottomLayout.addWidget(btn1)
        BottomLayout.addWidget(btn2)
        MainLayout.addLayout(TopLayout)
        MainLayout.addLayout(BottomLayout)
        self.setLayout(MainLayout)
        self.show()


def main():
    App = QApplication(sys.argv)
    window=Window()
    sys.exit(App.exec_())
if __name__ == '__main__':
    main()


