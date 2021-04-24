#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (
    QApplication,
    QLineEdit,
    QPushButton,
    QWidget,
    QLabel
)
from PyQt5.QtCore import Qt

class EntryWindow(QWidget):
    """QlineEdit Example."""
    
    def __init__(self):    #Constructor
        super().__init__() #Initializer which calls constructor for QWidget
        self.initializeUI() #Call function used to set up window
        
    def initializeUI(self):
        """ Initialize the Window and display contents to the screen."""
        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle('QLineEdit Widget')
        self.displayWidgets()
        
        self.show()
        
    def displayWidgets(self):
        """adds up the QlineEdit and other widgets.
        """
        
        # create name label and lineEdit widgets
        QLabel('Please enter your name below.', self).move(100, 10)
        name_label = QLabel('Name:', self)
        name_label.move(70, 50)
        
        self.name_edit = QLineEdit(self)
        # Read Observe listen and connect
        self.name_edit.setAlignment(Qt.AlignLeft) # Default alignment is left
        self.name_edit.move(130, 50)
        self.name_edit.resize(200, 20) # change size of entry field
        
        self.clr_button = QPushButton('Clear', self)
        self.clr_button.clicked.connect(self.clearEntries)
        self.clr_button.move(160, 110)
        
    def clearEntries(self):
        """ If button is pressed, clear the lineedit input field"""
        sender = self.sender()
        if sender.text() == 'Clear':
            self.name_edit.clear()
            
# Run the program
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EntryWindow()
    sys.exit(app.exec())