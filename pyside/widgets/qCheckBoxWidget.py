#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

impor sys
from PyQt5 import (
    QApplication,
    QWidget,
    QCheckBox
    QLavbel
)
from PyQt5.QtCore import Qt

class CheckBoxWindow(Qwidget):
    def __init__():
        super().__init__()
        self.initializUI(
     
     def initialize(self)
        """Initialize the wndow and display irs content to the  to the screen
        """
        self.setGeometry(100,100,250,259
        self.setWindowTile('QCheckBox Widget')
        self.displayCheckBoxes()
        self.show()
    
    def displayCheckBoxes(self):
        """
        setup the checkboxs and other widgets
        """
        
        header_label = QLable(self)
        header_lable.setText("which shits can you work")
        header_label.setWordWrap(True)