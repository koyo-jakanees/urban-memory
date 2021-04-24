#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton
)
from PyQt5.QtCore import pyqtSlot

class BtnWindow(QWidget):
    """create our gui constructs."""
    
    def __init__(self):
        super().__init__() #create default constructor fo QWidget
        self.initializeUI()
        
    def initializeUI(self):
        """set sup the button widget."""
        nm_label = QLabel(self)
        nm_label.setText('Don"t push the button.')
        nm_label.move(60, 30) # arrange label
        
        self.count_label = QLabel()
        self.count_label.setText('Push counts.')
        self.count_label.move(90, 100) # arrange label
        
        btn = QPushButton('Push me', self)
        btn.clicked.connect(self.btnClicked)
        btn.move(80, 70)
        self.show()
        
    @pyqtSlot()
    def btnClicked(self):
        """Print message to the terminal and close the window when clicked"""
        # self.count_label.setText(f'{i for i in range(10)}')
        print("The window has been closed")
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BtnWindow()
    sys.exit(app.exec_())