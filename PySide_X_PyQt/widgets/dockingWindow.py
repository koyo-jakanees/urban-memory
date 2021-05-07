# -*-coding:utf -*-
# see: https://pythonpyqt.com/qdockwidget/
#  see also: https://www.delftstack.com/tutorial/pyqt5/pyqt5-menubar/
# Dragable QDockable widget with a list inside it .

# imports
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QAction, QApplication, QDockWidget, QHBoxLayout,
                             QLabel, QListWidget, QMainWindow, QStyle,
                             QTextEdit, qApp)


class DockingWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle('Docky Docky')
        self.layout = QHBoxLayout()

        self.label = QLabel("The toggle state is ")
        self.label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label)


        # Add toggle action for checkable menu items
        toggleAction = QAction('&Toggle Label', self, checkable=True)        
        toggleAction.setStatusTip('Toggle the label')
        toggleAction.triggered.connect(self.toggleLabel)
        # Add action for quiting application
        exitAction = QAction(
            self.style().standardIcon(QStyle.SP_DialogCancelButton), 'Q&uit', self)
        # to use custom image icon, load using QIcon from QtGui as shown.
        # exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl + Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)
        
        # shows extra msg whenever user hovers the mouse poiner
        self.statusBar()
        # set up the menu items
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&File')
        fileMenu.addAction('New')
        fileMenu.addAction('S&ave')
        fileMenu.addAction(toggleAction)
        fileMenu.addAction(exitAction)

        self.items = QDockWidget('Dockers', self)

        self.listwidget = QListWidget()
        self.listwidget.addItem('Item1')
        self.listwidget.addItem('Item2')
        self.listwidget.addItem('Item3')
        self.listwidget.addItem('Item4')
        self.listwidget.addItem('Item5')
        self.listwidget.addItem('Item6')
        self.listwidget.addItem('Item7')

        # textEdit properties
        self.textEdit_value = QTextEdit()
        self.textEdit_value.textChanged.connect(self.save_text)

        self.items.setWidget(self.listwidget)
        self.items.setFloating(False)
        self.setCentralWidget(self.textEdit_value)
        self.addDockWidget(Qt.RightDockWidgetArea, self.items)

        # self.setLayout(layout)
        # commented out setting layout to surpress the warning: 
        # QWidget::setLayout: Attempting to set QLayout "" on DockingWindow "", which already has a layout

    def toggleLabel(self, state):
        self.label.setText("The toggle state is {}".format(state))

    def save_text(self):
        text = self.textEdit_value.toPlainText()
        with open('test.txt', 'w') as f:
            f.write(text)
def main():
    app = QApplication(sys.argv)
    dock = DockingWindow()
    dock.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()