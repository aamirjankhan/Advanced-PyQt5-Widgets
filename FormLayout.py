import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Form Layout")
        self.setGeometry(500 , 250 , 400 , 400)
        self.UI()
    def UI(self):
        formLayout=QFormLayout()
        #formLayout.setRowWrapPolicy(QFormLayout.WrapAllRows)
        self.setLayout(formLayout)
        hbox=QHBoxLayout()
        hbox.addWidget(QPushButton('Enter'))
        hbox.addWidget(QPushButton('Exit'))
        hbox.addStretch()
        hbox1=QHBoxLayout()
        hbox1.addWidget(QLineEdit())
        hbox1.addWidget(QLineEdit())
        name_text=QLabel('Name: ')
        name_input=QLineEdit()
        pass_text=QLabel('Password: ')
        pass_input=QLineEdit()
        formLayout.addRow(name_text,hbox1)
        formLayout.addRow(pass_text,pass_input)
        formLayout.addRow(QLabel('Country: '),QComboBox())
        formLayout.addRow(hbox)

        self.show()


def main():
    App = QApplication(sys.argv)
    window=Window()
    sys.exit(App.exec_())
if __name__ == '__main__':
    main()


