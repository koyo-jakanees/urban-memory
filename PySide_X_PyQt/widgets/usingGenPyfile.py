# -*- coding:utf-8 -*-
#  using generated py file by uic

import sys, random

from PySide2.QtWidgets import QApplication, QWidget

from .anotherWidget import Ui_Form


class NewWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_Form
        self.ui.setupUi(self)
        
        self.ui.button_add.clicked.connect(self.add_item)
        self.ui.button_remove.clicked.connect(self.remove_item)
        self.ui.button_clear.clicked.connect(self.clear_list)
        
    def add_item(self):
        self.ui.main_list.addItem(f"test {random.randint(0, 100)}")

    def remove_item(self):
        selected_items = self.ui.main_list.selectedItems()
        for item in selected_items:
            selection = self.ui.main_list.takeItem(self.ui.main_list.row(item))

    def clear_list(self):
        self.ui.main_list.clear()
        

if __name__ == "__main__":
    app = QApplication()
    window = NewWidget()
    window.show()
    sys.exit(app.exec_())