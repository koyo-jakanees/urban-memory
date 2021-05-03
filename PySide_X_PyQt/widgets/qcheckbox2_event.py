# -*-coding:utf-8 -*-
# ref: https://www.delftstack.com/tutorial/pyqt5/pyqt5-checkbox/

import sys
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QCheckBox,
    QHBoxLayout,
    QWidget
)
from PyQt5 import QtCore

class BasicWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

    def setupUi(self):
        layout = QHBoxLayout()
        self.setLayout(layout)
        
        self.checkBoxA = QCheckBox("Select This.")
        self.labelA = QLabel("Not slected.")
        
        self.checkBoxA.stateChanged.connect(self.checkBoxChangedAction)

        layout.addWidget(self.checkBoxA)
        layout.addWidget(self.labelA)
        
        self.setGeometry(200, 200, 300, 200)            
                
        self.setWindowTitle('CheckBox Example')
    
    def checkBoxChangedAction(self, state):
        if (QtCore.Qt.Checked == state):
            self.labelA.setText("Selected.")
        else:
            self.labelA.setText("Not Selected.")
    
def main():
    app = QApplication(sys.argv)
    windowExample = BasicWindow()
    windowExample.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()