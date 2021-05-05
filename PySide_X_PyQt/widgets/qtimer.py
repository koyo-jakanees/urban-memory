# -*- coding:utf-8 -*-
# QTimer Example
# The program below has a start and stop button. If you click the start button, it starts a QTimer
# see: https://pythonpyqt.com/qtimer/

import sys
from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QApplication,
    QListWidget,
    QGridLayout,
    QLabel
)
from PyQt5.QtCore import QTimer, QDateTime

class TimerWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle('QTimer in the working')
        self.listFile = QListWidget()
        self.label = QLabel('Timer')
        self.startBtn = QPushButton('start')
        self.endBtn = QPushButton('stop')
        
        # create a grid layout to add widgets later
        layout = QGridLayout()

        # create a timer object
        self.timer = QTimer()
        self.timer.timeout.connect(self.showTime)

        # add elements to the created layout
        layout.addWidget(self.label, 0, 0, 1, 2)
        layout.addWidget(self.startBtn, 1, 0)
        layout.addWidget(self.endBtn, 1, 1)

        self.startBtn.clicked.connect(self.startTimer)
        self.endBtn.clicked.connect(self.endTimer)

        # add every layout element to the QWidget
        self.setLayout(layout)

    def showTime(self):
        time = QDateTime.currentDateTime()
        displayTimer = time.toString('yyyy-MM-dd hh:mm:ss dddd')
        self.label.setText(displayTimer)
    
    def startTimer(self):
        self.timer.start(1000)
        self.startBtn.setEnabled(False)
        self.endBtn.setEnabled(True)

    def endTimer(self):
        self.timer.stop()
        self.startBtn.setEnabled(True)
        self.endBtn.setEnabled(False)

def main():
    app = QApplication(sys.argv)
    window = TimerWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()