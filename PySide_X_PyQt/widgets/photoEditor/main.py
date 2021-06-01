#! /usr/bin/env python
# -*-coding:utf-8 -*-

import sys
from PyQt5.QtCore import Qt, QSize, QRect
from PyQt5.QtGui import QIcon, QPixmap, QTransform, QPainter
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QAction,
    QFileDialog,
    QDesktopWidget,
    QMessageBox,
    QSizePolicy,
    QToolBar
)


class SimplePicEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        """Sets up the GUI's for the application and displays to screen"""
        self.setFixedSize(650, 650)
        self.setWindowTitle('Pic Editor')
        self.centerMainWindow()
        self.createToolsDockWidget()
        self.createMenu()
        self.createToolBar()
        self.photoEditorWidgets()

        self.show()

    def createMenu(self):
        """Generate Menu elements for the editor GUI"""
        # create menu actions for file menu: open, save and print image.
        self.open_action = QAction(QIcon('assets/open.png'), 'Open', self)
        self.open_action.setShortcut('Ctrl+O')
        self.open_action.setStatusTip('Open a new Image')
        self.open_action.triggered.connect(self.open_Image)

        self.save_action = QAction(QIcon('assets/save.png'), 'S&ave', self)
        self.save_action.setShortcut('Ctrl+S')
        self.save_action.setStatusTip('Save Image')
        self.save_action.triggered.connect(self.save_Image)

        self.print_action = QAction(QIcon('assets/print.png'), 'S&ave', self)
        self.print_action.setShortcut('Ctrl+P')
        self.print_action.setStatusTip('Print Image')
        self.print_action.triggered.connect(self.print_Image)