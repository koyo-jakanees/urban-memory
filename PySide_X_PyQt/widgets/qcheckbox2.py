# -*-coding:utf-8 -*-
# ref: https://www.delftstack.com/tutorial/pyqt5/pyqt5-checkbox/

import sys

from PyQt5.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
                             QWidget)


class BasicWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

    def setupUi(self):
        layout = QHBoxLayout()
        self.setLayout(layout)
        
        self.checkBoxA = QCheckBox("Select This.")
        self.labelA = QLabel("Not slected.")
        
        layout.addWidget(self.checkBoxA)
        layout.addWidget(self.labelA)
        
        self.setGeometry(200, 200, 300, 200)            
                
        self.setWindowTitle('CheckBox Example')
    
def main():
    app = QApplication(sys.argv)
    windowExample = BasicWindow()
    windowExample.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()