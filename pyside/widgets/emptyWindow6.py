#! /usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Get hands dirty with PySide6
"""
import sys
from PySide6.QtWidgets import QApplication, QWidget

class EmptyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
        
    def setupUi(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('PySide6 swimming through')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EmptyWindow()
    sys.exit(app.exec_())