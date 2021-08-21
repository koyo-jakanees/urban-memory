#! /usr/bin/env python
# -*- coding: utf-8 -*-
# original: begging pyqt

import sys
import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableWidget,
    QTableWidgetItem,
    QMenu,
    QAction,
    QInputDialog,
    QWidget)

class TableViewFramework(QMainWindow):
    
    # def __init__(self, parent: typing.Optional[QWidget], flags: typing.Union[QtCore.Qt.WindowFlags, QtCore.Qt.WindowType]) -> None:
    #     super().__init__(parent=parent, flags=flags)
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setMinimumSize(1000, 500)
        self.setWindowTitle("Data view test")
        
        # copy and paste actions
        self.item_text = None
        
        self.createMenu()
        self.createTable()
        self.show()

    def createTable(self):
        """Set up the table widget
        """
        self.table_wdgt = QTableWidget()
        
        # set up columns and rows
        self.table_wdgt.setRowCount(10)
        self.table_wdgt.setColumnCount(10)
        
        # set focus on cell 
        self.table_wdgt.setCurrentCell(0, 0)
        
        # emit signal when horizontal headers are clicked
        self.table_wdgt.horizontalHeader().sectionDoubleClicked.connect(
            self.changeHeader
        )
        self.setCentralWidget(self.table_wdgt)

    def createMenu(self):
        """Menu bar items set up and actions"""
        
        # actions
        quit_act = QAction('Quit', self)
        quit_act.setShortcut('Ctrl+Q')
        quit_act.triggered.connect(self.close)
        
        # copy & paste actions
        self.copy_cell = QAction('Copy', self)
        self.copy_cell.setShortcut('Ctrl+c')
        self.copy_cell.triggered.connect(self.copyItem)
        self.paste_cell = QAction('Paste', self)
        self.paste_cell.setShortcut('Ctrl+v')
        self.paste_cell.triggered.connect(self.copyItem)
        
        # Create table menu actions
        self.add_row_above_act = QAction("Add Row Above", self)
        self.add_row_above_act.setShortcut("Ctrl++")
        self.add_row_above_act.triggered.connect(self.addRowAbove)
        self.add_row_below_act = QAction("Add Row Below", self)
        self.add_row_below_act.triggered.connect(self.addRowBelow)
        self.add_col_before_act = QAction("Add Column Before", self)
        self.add_col_before_act.triggered.connect(self.addColumnBefore)
        self.add_col_after_act = QAction("Add Column After", self)
        self.add_col_after_act.triggered.connect(self.addColumnAfter)
        self.delete_row_act = QAction("Delete Row", self)
        self.delete_row_act.triggered.connect(self.deleteRow)
        self.delete_col_act = QAction("Delete Column", self)
        self.delete_col_act.triggered.connect(self.deleteColumn)
        self.clear_table_act = QAction("Clear All", self)
        self.clear_table_act.triggered.connect(self.clearTable)
        # Create the menu bar
        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False)
        # Create file menu and add actions
        file_menu = menu_bar.addMenu('File')
        file_menu.addAction(quit_act)
        # Create table menu and add actions
        table_menu = menu_bar.addMenu('Table')
        table_menu.addAction(self.add_row_above_act)
        table_menu.addAction(self.add_row_below_act)
        table_menu.addSeparator()
        table_menu.addAction(self.add_col_before_act)
        table_menu.addAction(self.add_col_after_act)
        table_menu.addSeparator()
        table_menu.addAction(self.delete_row_act)
        table_menu.addAction(self.delete_col_act)
        table_menu.addSeparator()
        table_menu.addAction(self.clear_table_act)

    def contextMenuEvent(self, event):
        """
        Create context menu and actions.
        """
        context_menu = QMenu(self)
        context_menu.addAction(self.add_row_above_act)
        context_menu.addAction(self.add_row_below_act)
        context_menu.addSeparator()
        context_menu.addAction(self.add_col_before_act)
        context_menu.addAction(self.add_col_after_act)
        context_menu.addSeparator()
        context_menu.addAction(self.delete_row_act)
        context_menu.addAction(self.delete_col_act)
        context_menu.addSeparator()
        context_menu.addAction(self.copy_cell)
        context_menu.addAction(self.paste_cell)
        context_menu.addSeparator()
        context_menu.addAction(self.clear_table_act)
        
        '''Execute the context_menu and return the action selected.
            mapToGlobal() translates the position of the window coordinates to
            the global screen coordinates. This way we can detect if a right-
            click occurred inside of the GUI and display the context menu
        '''
        action = context_menu.exec_(self.mapToGlobal(event.pos()))
        
        # To check for actions selected in the context menu that were not
        # created in the menu bar.
        if action == self.copy_cell:
            self.copyItem()
        if action == self.paste_cell:
            self.pasteItem()
        else:
            pass

    def keyPressEvent(self, event):
        """using key events to paste items
        ref:https://stackoverflow.com/questions/60715462/how-to-copy-and-paste-multiple-cells-in-qtablewidget-in-pyqt5
        """
        super().keyPressEvent(event)
        if event.key() == QtCore.Qt.Key_C and (event.modifiers() & QtCore.Qt.ControlModifier):
            self.copied_cells = sorted(self.table_wdgt.selectedIndexes())
        elif event.key() == QtCore.Qt.Key_V and (event.modifiers() & QtCore.Qt.ControlModifier):
            r = self.table_wdgt.currentRow() - self.copied_cells[0].row()
            c = self.table_wdgt.currentColumn() - self.copied_cells[0].column()
            for cell in self.copied_cells:
                self.table_wdgt.setItem(cell.row() + r, cell.column() + c, QTableWidgetItem(cell.data()))

    def copyItem(self):
        """
        If the current cell selected is not empty, store the text.
        """
        if self.table_wdgt.currentItem() != None:
            self.item_text = self.table_wdgt.currentItem().text()

    def pasteItem(self):
        """
        Set item for selected cell.
        """
        if self.item_text != None:
            row = self.table_wdgt.currentRow()
            column = self.table_wdgt.currentColumn()
            self.table_wdgt.setItem(
                row, column, QTableWidgetItem(self.item_text))

    def changeHeader(self):
        """
        Change horizontal headers by returning the text from input dialog.
        """
        col = self.table_wdgt.currentColumn()
        text, ok = QInputDialog.getText(self, "Enter Header", "Header text:")
        if ok and text != "":
            self.table_wdgt.setHorizontalHeaderItem(
                col, QTableWidgetItem(text))
        else:
            pass

    def addRowAbove(self):
        current_row = self.table_wdgt.currentRow()
        self.table_wdgt.insertRow(current_row)

    def addRowBelow(self):
        current_row = self.table_wdgt.currentRow()
        self.table_wdgt.insertRow(current_row + 1)

    def addColumnBefore(self):
        current_col = self.table_wdgt.currentColumn()
        self.table_wdgt.insertColumn(current_col)

    def addColumnAfter(self):
        current_col = self.table_wdgt.currentColumn()
        self.table_wdgt.insertColumn(current_col + 1)

    def deleteRow(self):
        current_row = self.table_wdgt.currentRow()
        self.table_wdgt.removeRow(current_row)

    def deleteColumn(self):
        current_col = self.table_wdgt.currentColumn()
        self.table_wdgt.removeColumn(current_col)

    def clearTable(self):
        self.table_widget.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TableViewFramework()
    sys.exit(app.exec_())
