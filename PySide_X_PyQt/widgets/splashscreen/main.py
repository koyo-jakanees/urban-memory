#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 08:50:05 2021
ref: https://youtu.be/LSKbjuWvoN4
"""

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# Ui imports
from ui_MainWindow import Ui_MainWindow
from ui_splashscreen import Ui_splashScreen

# splash screen
class SplashSCreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_splashScreen()
        self.ui.setupUi(self)

        self.show()
        
# Main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()