# -*-coding:utf-8 -*-
# ref: https://pythonbasics.org/qcheckbox/

import sys
from PyQt5.QtWidgets import (
    QWidget,
    QGridLayout,
    QCheckBox,
    QApplication
)

class Window(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()
    
    def setupUi(self):
        layout = QGridLayout()
        self.setLayout(layout)

        checkBtn = QCheckBox('I have a cat')
        checkBtn.setChecked(True)
        checkBtn.animal = 'Cat'
        checkBtn.toggled.connect(self.onClicked)
        layout.addWidget(checkBtn, 0, 0)

    def onClicked(self):
        checkBtn = self.sender()
        print("Animal " + (checkBtn.animal) + " is " + str(checkBtn.isChecked()))

def main():
    app = QApplication(sys.argv)
    screen = Window()
    screen.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()