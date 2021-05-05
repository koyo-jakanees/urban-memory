# -*-coding:utf-8 -*-
# ref: https://pythonbasics.org/qdial/

import sys

from PyQt5.QtWidgets import QApplication, QDial, QGridLayout, QLabel, QWidget


class QdialWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

    def setupUi(self):
        layout = QGridLayout()
        self.setLayout(layout)
        self.dial = QDial()
        self.dial.setMinimum(0)
        self.dial.setMaximum(100)
        self.dial. setValue(0)
        self.dial.valueChanged.connect(self.dialerMoved)
        self.label = QLabel("0")
        
        layout.addWidget(self.dial)
        layout.addWidget(self.label)
        self.show()
    
    def dialerMoved(self):
        print(f'Dial Value is : {self.dial.value()}')
        self.label.setText(f'Dial Value is : {self.dial.value()}')

def main():
    app = QApplication(sys.argv)
    window = QdialWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()