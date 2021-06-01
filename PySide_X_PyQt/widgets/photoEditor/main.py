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
    QDockWidget,
    QToolBar,
    QStatusBar,
    QPushButton,
    QVBoxLayout
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
        self.open_action = QAction(QIcon('assets/open.png'), '&Open', self)
        self.open_action.setShortcut('Ctrl+O')
        self.open_action.setStatusTip('Open a new Image')
        self.open_action.triggered.connect(self.open_Image)

        self.save_action = QAction(QIcon('assets/save.png'), 'S&ave', self)
        self.save_action.setShortcut('Ctrl+S')
        self.save_action.setStatusTip('Save Image')
        self.save_action.triggered.connect(self.save_Image)

        self.print_action = QAction(QIcon('assets/print.png'), 'Print', self)
        self.print_action.setShortcut('Ctrl+P')
        self.print_action.setStatusTip('Print Image')
        self.print_action.triggered.connect(self.print_Image)

        self.exit_action = QAction(QIcon('assets/exit.png'), 'Exit', self)
        self.exit_action.setShortcut('Ctrl+Q')
        self.exit_action.setStatusTip('Quit Program')
        self.exit_action.triggered.connect(self.close)

        self.clear_action = QAction(QIcon('assets/clear.png'), 'Clear Image', self)
        self.clear_action.setShortcut('Ctrl+D')
        self.clear_action.setStatusTip('Clear the current Image')
        self.clear_action.triggered.connect(self.clear_Image)

        # edit menu actions i.e rotating, flipping actions

        self.rotate90_action = QAction('Rotate 90°', self)
        self.rotate90_action.setStatusTip('Rotate image 90° clockwise')
        self.rotate90_action.triggered.connect(self.rotate_image90)

        self.rotate180_action = QAction('Rotate 180°', self)
        self.rotate180_action.setStatusTip('Rotate image 180° clockwise')
        self.rotate180_action.triggered.connect(self.rotate_image180)

        self.hor_flip_action = QAction('Flip Horizontal°', self)
        self.hor_flip_action.setStatusTip('Flip Image across Horizontal axis')
        self.hor_flip_action.triggered.connect(self.flip_horizontal)

        self.vert_flip_action = QAction('Flip Vertical', self)
        self.vert_flip_action.setStatusTip('Flip Image across Vertical Axis')
        self.vert_flip_action.triggered.connect(self.flip_vertical)

        self.resize_action = QAction('Resize Half', self)
        self.resize_action.setStatusTip(
            'Resize Image to half the original size')
        self.resize_action.triggered.connect(self.resize_half)

        # Menu bar for the application
        bar_menu = self.menuBar()
        bar_menu.setNativeMenuBar(False)

        # create file menu and add the actions above
        file_menu = bar_menu.addMenu('File')
        file_menu.addAction(self.open_action)
        file_menu.addAction(self.save_action)
        file_menu.addSeparator()
        file_menu.addAction(self.print_action)
        file_menu.addSeparator()
        file_menu.addAction(self.exit_action)

        # create edit menu and add the actions above
        edit_menu = bar_menu.addMenu('Edit')
        edit_menu.addAction(self.rotate180_action)
        edit_menu.addAction(self.rotate180_action)
        edit_menu.addSeparator()
        edit_menu.addAction(self.hor_flip_action)
        edit_menu.addAction(self.vert_flip_action)
        edit_menu.addSeparator()
        edit_menu.addAction(self.resize_action)
        edit_menu.addSeparator()
        edit_menu.addAction(self.clear_action)

        # Create view menu and add actions
        view_menu = bar_menu.addMenu('View')
        view_menu.addAction(self.toggle_dock_tools_act)
        # Display info about tools, menu, and view in the status bar
        self.setStatusBar(QStatusBar(self))

    def createToolBar(self):
        """Create toolbar for photo editor GUI"""
        tool_bar = QToolBar("Photo Editor Toolbar")
        tool_bar.setIconSize(QSize(24, 24))
        self.addToolBar(tool_bar)

        # Add actions to toolbar
        tool_bar.addAction(self.open_act)
        tool_bar.addAction(self.save_act)
        tool_bar.addAction(self.print_act)
        tool_bar.addAction(self.clear_act)
        tool_bar.addSeparator()
        tool_bar.addAction(self.exit_act)

    def createToolsDockWidget(self):
        """Use View -> Edit Image Tools menu and click the dock widget on or off.
        Tools dock can be placed on the left or right of the main window.
        """
        # Set up QDockWidget
        self.dock_tools_view = QDockWidget()
        self.dock_tools_view.setWindowTitle("Edit Image Tools")
        self.dock_tools_view.setAllowedAreas(
            Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        # Create container QWidget to hold all widgets inside dock widget
        self.tools_contents = QWidget()
        # Create tool push buttons
        self.rotate90_btn = QPushButton("Rotate 90°")
        self.rotate90_btn.setMinimumSize(QSize(130, 40))
        self.rotate90_btn.setStatusTip('Rotate image 90° clockwise')
        self.rotate90_btn.clicked.connect(self.rotate_image90)
        self.rotate180_btn = QPushButton("Rotate 180°")
        self.rotate180_btn.setMinimumSize(QSize(130, 40))
        self.rotate180_btn.setStatusTip('Rotate image 180° clockwise')
        self.rotate180_btn.clicked.connect(self.rotate_image180)
        self.flip_horizontal_btn = QPushButton("Flip Horizontal")
        self.flip_horizontal_btn.setMinimumSize(QSize(130, 40))
        self.flip_horizontal_btn.setStatusTip(
            'Flip image across horizontal axis')
        self.flip_horizontal_btn.clicked.connect(self.flip_horizontal)
        self.flip_vertical_btn = QPushButton("Flip Vertical")
        self.flip_vertical_btn.setMinimumSize(QSize(130, 40))
        self.flip_vertical_btn.setStatusTip('Flip image across vertical axis')
        self.flip_vertical_btn.clicked.connect(self.flip_vertical)
        self.resize_half_btn = QPushButton("Resize Half")
        self.resize_half_btn.setMinimumSize(QSize(130, 40))
        self.resize_half_btn.setStatusTip(
            'Resize image to half the original size')
        self.resize_half_btn.clicked.connect(self.resize_half)
        # Set up vertical layout to contain all the push buttons
        dock_v_box = QVBoxLayout()
        dock_v_box.addWidget(self.rotate90)
        dock_v_box.addWidget(self.rotate180)
        dock_v_box.addStretch(1)
        dock_v_box.addWidget(self.flip_horizontal)
        dock_v_box.addWidget(self.flip_vertical)
        dock_v_box.addStretch(1)
        dock_v_box.addWidget(self.resize_half)
        dock_v_box.addStretch(6)
        # Set the main layout for the QWidget, tools_contents,
        # then set the main widget of the dock widget
        self.tools_contents.setLayout(dock_v_box)
        self.dock_tools_view.setWidget(self.tools_contents)
        # Set initial location of dock widget
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock_tools_view)
        # Handles the visibility of the dock widget 
        self.toggle_dock_tools_act = self.dock_tools_view.toggleViewAction()

    def photoEditorWidgets(self):
        """
        Set up instances of widgets for photo editor GUI
        """
        self.image = QPixmap()
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        # Use setSizePolicy to specify how the widget can be resized,
        # horizontally and vertically. Here, the image will stretch
        # horizontally, but not vertically.
        self.image_label.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Ignored)
        self.setCentralWidget(self.image_label)

    def open_Image(self):
        """
        Open an image file and display its contents in label widget.
        Display error message if image can't be opened.
        """
        image_file, _ = QFileDialog.getOpenFileName(
            self, "Open Image", "",
            "JPG Files (*.jpeg *.jpg );;PNG Files (*.png);;Bitmap Files(*.bmp);;\
                GIF Files (*.gif)")
        if image_file:
            self.image = QPixmap(image_file)
            self.image_label.setPixmap(
                self.image.scaled(
                    self.image_label.size(),
                    Qt.KeepAspectRatio, Qt.SmoothTransformation))
        else:
            QMessageBox.information(
                self, "Error", "Unable to open image.", QMessageBox.Ok)
        self.print_action.setEnabled(True)

    def save_Image(self):
        """
        Save the image.
        Display error message if image can't be saved.
        """
        image_file, _ = QFileDialog.getSaveFileName(
            self, "Save Image", "",
            "JPG Files (*.jpeg *.jpg );;PNG Files (*.png);;Bitmap Files(*.bmp);;\
            GIF Files (*.gif)")
        if image_file and self.image.isNull() is False:
            self.image.save(image_file)
        else:
            QMessageBox.information(self, "Error", "Unable to save image.",
                                    QMessageBox.Ok)

    def clear_Image(self):
        """
        Clears current image in QLabel widget
        """
        self.image_label.clear()
        self.image = QPixmap()  # reset pixmap so that isNull() = True

    def print_Image(self):
        """
        Print image.
        """
        # Create printer object and print output defined by the platform
        # the program is being run on.
        # QPrinter.NativeFormat is the default
        printer = QPrinter()
        printer.setOutputFormat(QPrinter.NativeFormat)
        # Create printer dialog to configure printer
        print_dialog = QPrintDialog(printer)
        # If the dialog is accepted by the user, begin printing
        if (print_dialog.exec_() == QPrintDialog.Accepted):
            # Use QPainter to output a PDF file
            painter = QPainter()
            # Begin painting device
            painter.begin(printer)
            # Set QRect to hold painter's current viewport, which
            # is the image_label
            rect = QRect(painter.viewport())
            # Get the size of image_label and use it to set the size
            # of the viewport
            size = QSize(self.image_label.pixmap().size())
            size.scale(rect.size(), Qt.KeepAspectRatio)
            painter.setViewport(
                rect.x(), rect.y(), size.width(), size.height())
            painter.setWindow(self.image_label.pixmap().rect())
            # Scale the image_label to fit the rect source (0, 0)
            painter.drawPixmap(0, 0, self.image_label.pixmap())
            # End painting
            painter.end()

    def rotate_image90(self):
        """
        Rotate image 90° clockwise
        """
        if self.image.isNull() is False:
            transform90 = QTransform().rotate(90)
            pixmap = QPixmap(self.image)
            rotated = pixmap.transformed(
                transform90, mode=Qt.SmoothTransformation)
            self.image_label.setPixmap(
                rotated.scaled(
                    self.image_label.size(),
                    Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.image = QPixmap(rotated)
            self.image_label.repaint()  # repaint the child widget
        else:
            # No ima
            pass

    def rotate_image180(self):
        """
        Rotate image 180° clockwise
        """
        if self.image.isNull() is False:
            transform180 = QTransform().rotate(180)
            pixmap = QPixmap(self.image)
            rotated = pixmap.transformed(
                transform180, mode=Qt.SmoothTransformation)
            self.image_label.setPixmap(
                rotated.scaled(
                    self.image_label.size(),
                    Qt.KeepAspectRatio, Qt.SmoothTransformation))
            # In order to keep being allowed to rotate the image, set the
            # rotated image as self.image
            self.image = QPixmap(rotated)
            self.image_label.repaint()  # repaint the child widget
        else:
            # No image to rotate
            pass

    def flip_horizontal(self):
        """
        Mirror the image across the horizontal axis
        """
        if self.image.isNull() is False:
            flip_h = QTransform().scale(-1, 1)
            pixmap = QPixmap(self.image)
            flipped = pixmap.transformed(flip_h)
            self.image_label.setPixmap(
                flipped.scaled(
                    self.image_label.size(),
                    Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.image = QPixmap(flipped)
            self.image_label.repaint()
        else:
            # no image flip
            pass
        