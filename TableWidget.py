import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Tableb Widget")
        self.setGeometry(500 , 250 , 400 , 400)
        self.UI()

    def UI(self):
        vbox=QVBoxLayout()
        self.table=QTableWidget()
        self.table.setRowCount(5)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderItem(0,QTableWidgetItem('Name'))
        self.table.setHorizontalHeaderItem(1,QTableWidgetItem('Surname'))
        self.table.setHorizontalHeaderItem(2,QTableWidgetItem('Address'))
        self.table.setItem(0,0,QTableWidgetItem('First Entry'))
        self.table.setItem(1,1,QTableWidgetItem('Second Entry'))
        self.table.setItem(2,2,QTableWidgetItem('Third Entry'))
        self.table.setItem(3,2,QTableWidgetItem('Fourth Entry'))
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        #self.table.horizontalHeader().hide()
        #self.table.verticalHeader().hide()
        vbox.addWidget(self.table)
        self.setLayout(vbox)
        btn1=QPushButton('Get')
        vbox.addWidget(btn1)
        btn1.clicked.connect(self.getValue)
        self.table.doubleClicked.connect(self.doubleClicked)
        self.show()

    def getValue(self):
        for item in self.table.selectedItems():
            print(item.text(),item.row(),item.column())

    def doubleClicked(self):
        for item in self.table.selectedItems():
            print(item.text(),item.row(),item.column())

def main():
    App = QApplication(sys.argv)
    window=Window()
    sys.exit(App.exec_())
if __name__ == '__main__':
    main()

