import random
import sys

from PySide2.QtCore import QFile, QIODevice
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication


def add_item():
    window.main_list.addItem(f"test {random.randint(0, 100)}")


def remove_item():
    selected_items = window.main_list.selectedItems()
    for item in selected_items:
        window.main_list.takeItem(window.main_list.row(item))


def clear_list():
    window.main_list.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ui_file = QFile("./PySide_X_PyQt/widgets/anotherWidget.ui")
    if not ui_file.open(QIODevice.ReadOnly):
        print("Cannot open {}: {}".format(ui_file, ui_file.errorString()))
        sys.exit(-1)
    loader = QUiLoader()
    window = loader.load(ui_file, None)
    ui_file.close()

    window.button_add.clicked.connect(add_item)
    window.button_remove.clicked.connect(remove_item)
    window.button_clear.clicked.connect(clear_list)

    if not window:
        print(loader.errorString())
        sys.exit(-1)
    window.show()

    sys.exit(app.exec_())
