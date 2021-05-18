#! /usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Get hands dirty with PySide6
random online so=nippets, not my work to license
"""
import sys

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QLabel, QWidget


class EmptyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
        
    def setupUi(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('PySide6 swimming through')
        self.displayLabels()
        self.show()
        
    def displayLabels(self):
        """Display text and images using qlabels
        catch err if file doesn't exist
        """
        txt = QLabel(self)
        txt.setText('Hello Yoda')
        txt.move(105, 15)
        
        img = '../../img/snippet.png'
        try:
            with open(img):
                code_img = QLabel(self)
                pixmap = QPixmap(img)
                code_img.setPixmap(pixmap)
                code_img.move(25, 40)
        except FileNotFoundError:
            print("Image file not found!!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EmptyWindow()
    sys.exit(app.exec_())