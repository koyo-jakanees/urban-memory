# -*-coding:utf-8 -*-
"""
Implementing variants of progress bar beautification.
Progress bar helps indicate to the user the status of a long running process
thus enhances the User experience of the application. At times this may cause
the main Ui of the whole application to freeze or unresponsive. The freezing 
problem can be  handled well through Qthread. see 'freezingGui.py' script
ref: https://pythonpyqt.com/pyqt-progressbar/
"""

# QProgressBar Example.
# 1. use the time module to delay operation time.sleep()
# 2. put delay operation into a subthread to demo UI refresh of PyQt
# thread will be updating the QProgressBar, doesn't cause main thread to hang.

import sys
import time
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QProgressBar,
    QVBoxLayout,
    QApplication
)

class Thread(QThread):
    """run different threads"""
    _signal = pyqtSignal(int)
    def __init__(self):
        super(Thread, self).__init__()

    def __del__(self):
        self.wait()
    
    def run(self):
        for i in range(50):
            time.sleep(0.1)
            self._signal.emit(i)

class ProgressExample(QWidget):
    """The main ui components"""
    def __init__(self, parent=None):
        super(ProgressExample, self).__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle('QProgressBar Example')
        self.btn = QPushButton('Click Me!')
        self.btn.clicked.connect(self.btnFunc)
        self.pBar = QProgressBar()
        self.pBar.setValue(0)
        self.resize(300, 100)
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.pBar)
        self.vbox.addWidget(self.btn)
        self.setLayout(self.vbox)
        self.show()

    def btnFunc(self):
        self.thread = Thread()
        self.thread._signal.connect(self.signal_accept)
        self.thread.start()
        self.btn.setEnabled(False)

    def signal_accept(self, msg):
        self.pBar.setValue(int(msg))
        if self.pBar.value() == 99:
            self.pBar.setValue(0)
            self.btn.setEnabled(True)

def main():
    app = QApplication(sys.argv)
    window = ProgressExample()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()