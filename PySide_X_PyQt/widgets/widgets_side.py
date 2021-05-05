#-*-coding:utf-8 -*-

import random
import sys

from PySide2.QtCore import Slot
from PySide2.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
                               QWidget)

"""
a widget with code only without using external ui files
QPushButton  connects to a slot
"""

class Widget(QWidget):
    def __init__(self, parent=None) -> None:
        super(Widget, self).__init__(parent)
        self.button = QPushButton('Random Number')
        self.label = QLabel('0')
        
        self.button.clicked.connect(self.random_num)
        
        layout = QHBoxLayout()
        layout.addWidget(self.label, 1)
        layout.addWidget(self. button, 2)
        
        self.setLayout(layout)
        
    @Slot()
    def random_num(self):
        self.label.setText(f'{random.randint(0, 100)}')
        
if __name__ == "__main__":
    app = QApplication()
    widget = Widget()
    widget.resize(800, 400)
    widget.show()
    sys.exit(app.exec_())