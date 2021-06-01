#! /usr/bin/env python
# -*-coding:utf-8 -*-

import sys
import math
from PyQt5.QtCore import Qt, QSize, QRect
from PyQt5.QtGui import QIcon, QPalette, QPixmap, QTransform, QPainter
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
    QVBoxLayout,
    qApp,
    QScrollArea
)


class SimplePicEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.scaleFactor = 0.0

    def setupUi(self):
        """Sets up the GUI's for the application and displays to screen"""
        self.setFixedSize(650, 650)
        self.setWindowTitle('Pic Editor')
        self.centerMainWindow()
        self.createToolsDockWidget()
        self.createMenu()
        # self.createActions()
        self.createToolBar()
        self.photoEditorWidgets()
        self.resize(800, 800)

        self.show()

    def createMenu(self):
        """Generate Menu elements for the editor GUI"""
        # create menu actions for file menu: open, save and print image.
        self.open_action = QAction(
            QIcon('assets/open.png'), '&Open', self)
        self.open_action.setShortcut('Ctrl+O')
        self.open_action.setStatusTip('Open a new Image')
        self.open_action.triggered.connect(self.open_Image)

        self.save_action = QAction(
            QIcon('assets/save.png'), 'S&ave', self)
        self.save_action.setShortcut('Ctrl+S')
        self.save_action.setStatusTip('Save Image')
        self.save_action.triggered.connect(self.save_Image)

        self.print_action = QAction(
            QIcon('assets/print.png'), 'Print', self)
        self.print_action.setShortcut('Ctrl+P')
        self.print_action.setStatusTip('Print Image')
        self.print_action.triggered.connect(self.print_Image)

        self.exit_action = QAction(
            QIcon('assets/exit.png'), 'Exit', self)
        self.exit_action.setShortcut('Ctrl+Q')
        self.exit_action.setStatusTip('Quit Program')
        self.exit_action.triggered.connect(self.close)

        self.clear_action = QAction(
            QIcon('assets/clear.png'), 'Clear Image', self)
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

        self.hor_flip_action = QAction('Flip Horizontal', self)
        self.hor_flip_action.setStatusTip('Flip Image across Horizontal axis')
        self.hor_flip_action.triggered.connect(self.flip_horizontal)

        self.vert_flip_action = QAction('Flip Vertical', self)
        self.vert_flip_action.setStatusTip('Flip Image across Vertical Axis')
        self.vert_flip_action.triggered.connect(self.flip_vertical)

        self.resize_action = QAction('Resize Half', self)
        self.resize_action.setStatusTip(
            'Resize Image to half the original size')
        self.resize_action.triggered.connect(self.resize_half)

        self.fit_to_window_action = QAction(
            '&Fit to window', self, checkable=True)
        self.fit_to_window_action.setEnabled(False)
        self.fit_to_window_action.setShortcut('Ctrl+F')
        self.fit_to_window_action.setStatusTip(
            'Fit image to window size'
        )
        self.fit_to_window_action.triggered.connect(self.fit_to_window)

        self.zoomIn_action = QAction(
            QIcon('assets/zoomIn.png'), 'Zoom &In (25%)', self)
        self.zoomIn_action.setEnabled(False)
        self.zoomIn_action.setShortcut('Ctrl++')
        self.zoomIn_action.setStatusTip(
            'Zoom in on image'
        )
        self.zoomIn_action.triggered.connect(self.zoomIn)

        self.zoomOut_action = QAction(
            QIcon('assets/zoomout.png'), 'Zoom &Out (25%)', self)
        self.zoomOut_action.setEnabled(False)
        self.zoomOut_action.setShortcut('Ctrl+-')
        self.zoomOut_action.setStatusTip(
            'Zoom out image'
        )
        self.zoomOut_action.triggered.connect(self.zoomOut)

        self.about_action = QAction('&About', self, triggered=self.about)
        self.aboutQt_action = QAction(
            'About &Qt', self, triggered=qApp.aboutQt)

        self.normalSize_action = QAction(
            '&Normal Size', self, shortcut="Ctrl+J", enabled=False,
            triggered=self.normalSize)

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
        edit_menu.addAction(self.rotate90_action)
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
        view_menu.addAction(self.zoomIn_action)
        view_menu.addAction(self.zoomOut_action)
        view_menu.addAction(self.normalSize_action)
        view_menu.addSeparator()
        view_menu.addAction(self.fit_to_window_action)
        view_menu.addSeparator()
        view_menu.addAction(self.toggle_dock_tools_act)

        # create help menu and actions
        help_menu = bar_menu.addMenu('&Help')
        help_menu.addAction(self.about_action)
        help_menu.addSeparator()
        help_menu.addAction(self.aboutQt_action)
        # Display info about tools, menu, and view in the status bar
        self.setStatusBar(QStatusBar(self))

    def updateActions(self):
        self.zoomIn_action.setEnabled(not self.fit_to_window_action.isChecked())
        self.zoomOut_action.setEnabled(not self.fit_to_window_action.isChecked())
        self.normalSize_action.setEnabled(not self.fit_to_window_action.isChecked())

    def createToolBar(self):
        """Create toolbar for photo editor GUI"""
        tool_bar = QToolBar("Photo Editor Toolbar")
        tool_bar.setIconSize(QSize(24, 24))
        self.addToolBar(tool_bar)

        # Add actions to toolbar
        tool_bar.addAction(self.open_action)
        tool_bar.addAction(self.save_action)
        tool_bar.addSeparator()
        tool_bar.addAction(self.print_action)
        tool_bar.addAction(self.clear_action)
        tool_bar.addSeparator()
        tool_bar.addAction(self.exit_action)
        tool_bar.addSeparator()
        tool_bar.addAction(self.zoomIn_action)
        tool_bar.addAction(self.zoomOut_action)

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
        dock_v_box.addWidget(self.rotate90_btn)
        dock_v_box.addWidget(self.rotate180_btn)
        dock_v_box.addStretch(1)
        dock_v_box.addWidget(self.flip_horizontal_btn)
        dock_v_box.addWidget(self.flip_vertical_btn)
        dock_v_box.addStretch(1)
        dock_v_box.addWidget(self.resize_half_btn)
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
        self.scrollArea = QScrollArea()
        self.image_label.setAlignment(Qt.AlignCenter)
        # Use setSizePolicy to specify how the widget can be resized,
        # horizontally and vertically. Here, the image will stretch
        # horizontally, but not vertically.
        self.image_label.setBackgroundRole(QPalette.Base)
        self.image_label.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Ignored)
        self.image_label.setScaledContents(True)
        self.scrollArea.setBackgroundRole(QPalette.Dark)
        self.scrollArea.setWidget(self.image_label)
        self.scrollArea.setVisible(False)
        self.setCentralWidget(self.scrollArea)

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
        self.scaleFactor = 1.0
        self.scrollArea.setVisible(True)
        self.fit_to_window_action.setEnabled(True)
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

    def fit_to_window(self):
        fit_to_window = self.fit_to_window_action.isChecked()
        self.scrollArea.setWidgetResizable(fit_to_window)
        if not fit_to_window:
            self.normalSize()

        self.updateActions()

    def zoomIn(self):
        self.scaleImage(1.25)

    def zoomOut(self):
        self.scaleImage(0.8)

    def normalSize(self):
        self.image_label.adjustSize()
        self.scaleFactor = 1.0

    def about(self):
        QMessageBox.about(
            self, 'About Simple Pic Editor',
            '<p>The <b>Simple Pic</b> Editor shows how to use different'
            'widgets offere in Qt bindings to python to create a simple'
            'image editor and viewer.</p>'
            'QLabel and QScrollArea to display an image. QLabel is '
            'typically used for displaying text, but it can also display'
            'an image. QScrollArea provides a scrolling view around'
            'another widget. If the child widget exceeds the size of the '
            'frame, QScrollArea automatically provides scroll bars.</p>'
            '<p>The example demonstrates how QLabel"s ability to scale '
            'its contents (QLabel.scaledContents), and QScrollArea"s'
            'ability to automatically resize its contents '
            '(QScrollArea.widgetResizable), can be used to implement '
            'zooming and scaling features.</p>'
            '<p>In addition the example shows how to use QPainter to '
            'print an image.</p>')

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
        if not self.image.isNull():
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

    def flip_vertical(self):
        """
        Mirror the image across the Vertical axis
        """
        if not self.image.isNull():
            flip_v = QTransform().scale(1, -1)
            pixmap = QPixmap(self.image)
            flipped = pixmap.transformed(flip_v)
            self.image_label.setPixmap(
                flipped.scaled(
                    self.image_label.size(),
                    Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.image = QPixmap(flipped)
            self.image_label.repaint()
        else:
            # no image flip
            pass

    def resize_half(self):
        """
        Resize the image to half its current size.
        """
        if not self.image.isNull():
            resize = QTransform().scale(0.5, 0.5)
            pixmap = QPixmap(self.image)
            resized = pixmap.transformed(resize)
            self.image_label.setPixmap(
                resized.scaled(
                    self.image_label.size(),
                    Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.image = QPixmap(resized)
            self.image_label.repaint()
        else:
            # no image to resize
            pass

    def scaleImage(self, factor):
        self.scaleFactor *= factor
        self.image_label.resize(
            self.scaleFactor * self.image_label.pixmap().size())

        self.adjustScrollBar(self.scrollArea.horizontalScrollBar(), factor)
        self.adjustScrollBar(self.scrollArea.verticalScrollBar(), factor)

        self.zoomIn_action.setEnabled(self.scaleFactor < 3.0)
        self.zoomOut_action.setEnabled(self.scaleFactor > 0.333)

    def adjustScrollBar(self, scrollBar, factor):
        scrollBar.setValue(int(factor * scrollBar.value()
                               + ((factor - 1) * scrollBar.pageStep() / 2)))

    def centerMainWindow(self):
        """
        Use QDesktopWidget class to access information about your screen
        and use it to center the application window.
        """
        desktop = QDesktopWidget().screenGeometry()
        screen_width = desktop.width()
        screen_height = desktop.height()
        self.move(
            math.ceil((screen_width - self.width()) / 2),
            math.ceil((screen_height - self.height()) / 2))


# main function to run the program and call the pic Editor
def main():
    app = QApplication(sys.argv)
    app.setAttribute(Qt.AA_DontShowIconsInMenus, True)
    win = SimplePicEditor()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

# Improvements:
# https://gist.github.com/acbetter/32c575803ec361c3e82064e60db4e3e0
# https://github.com/baoboa/pyqt5/blob/master/examples/widgets/imageviewer.py
# https://gist.github.com/acbetter/e7d0c600fdc0865f4b0ee05a17b858f2
