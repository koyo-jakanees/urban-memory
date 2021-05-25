#!/usr/bin/env python
# -*-coding:utf-8 -*-

# source blog: https://www.mfitzp.com/tutorials/qprocess-external-programs/
# running background programs without impacting ui.
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QPlainTextEdit,
                                QVBoxLayout, QWidget)
from PyQt5.QtCore import QProcess
import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.btn = QPushButton("Execute")
        self.btn.pressed.connect(self.start_process)
        self.text = QPlainTextEdit()
        self.text.setReadOnly(True)

        l = QVBoxLayout()
        l.addWidget(self.btn)
        l.addWidget(self.text)

        w = QWidget()
        w.setLayout(l)

        self.setCentralWidget(w)

    def start_process(self):
        # We'll run our process here.
        pass

app = QApplication(sys.argv)

w = MainWindow()
w.show()

app.exec_()