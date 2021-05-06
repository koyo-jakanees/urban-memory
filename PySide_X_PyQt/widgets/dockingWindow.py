# -*-coding:utf -*-
# see: https://pythonpyqt.com/qdockwidget/
#  see also: https://www.delftstack.com/tutorial/pyqt5/pyqt5-menubar/
# Dragable QDockable widget with a list inside it .

# imports
import sys
from PyQt5.QtWidgets import (
    QDockWidget,
    QHBoxLayout,
    QListWidget,
    QMainWindow,
    QTextEdit,
    QApplication,
    QAction,
    qApp,
    QStyle
)
from PyQt5.QtCore import Qt

class DockingWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle('Docky Docky')
        layout = QHBoxLayout()
        
        # Add action for quiting application
        exitAction = QAction(
            self.style().standardIcon(QStyle.SP_DialogCancelButton), 'Q&uit', self)
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

        self.items.setWidget(self.listwidget)
        self.items.setFloating(False)
        self.setCentralWidget(QTextEdit())
        self.addDockWidget(Qt.RightDockWidgetArea, self.items)

        self.setLayout(layout)

def main():
    app = QApplication(sys.argv)
    dock = DockingWindow()
    dock.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()