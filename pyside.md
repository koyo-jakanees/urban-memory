<!-- widgets developed using PySide 2 or 6 and pyqt -->
# Pyside X PyQt development for rapid GUIs

Edit: the book **Beginning PyQt** is also a good start point and 
some of the snippets here are derived from the book too. The book also contain _code Explantion_ section which concised describes what each line  of code does.

Since both PySide and PyQt are python bindings to the  Qt C++ framework, generated using Shiboken and Sip respctively; they have subtle differences.
Most common ones would be in the naming of generated classes and modules e.g in imports
`PySide`: by Qt company (Qt for Python project)
`PyQt`: by RiverBank computing

```python
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
```

```python
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader
```

Converting `.ui` files to python
for PyQt5-uic:

```bash
pyuic5 mainwindow.ui -o MainWindow.py
```

for pyside2-uic:

```bash
pyside2-uic mainwindow.ui -o MainWindow.py
```

One should take keen note on Qt's `signal and slot` calls and naming. they use different syntax.

syntactical difference
signals:

```python
# https://www.mfitzp.com/news/pyqt5-vs-pyside2/
my_custom_signal = pyqtSignal()  # PyQt5
my_custom_signal = Signal()  # PySide2

my_other_signal = pyqtSignal(int)  # PyQt5
my_other_signal = Signal(int)  # PySide2
```

Slots:

```python
@pyqtslot
def my_custom_slot():
    pass

@Slot
def my_custom_slot():
    pass
```

If writing a software that requires compatibility with both libraries;
consider adding both sets in the import (the naive approach)

snippet source and ref: [Martin Fitzpatrick](https://www.mfitzp.com/news/pyqt5-vs-pyside2/)

```python
import sys

# The contents of the qt.py
if 'PyQt5' in sys.modules:
    # PyQt5
    from PyQt5 import QtGui, QtWidgets, QtCore
    from PyQt5.QtCore import pyqtSignal as Signal, pyqtSlot as Slot

else:
    # PySide2
    from PySide2 import QtGui, QtWidgets, QtCore
    from PySide2.QtCore import Signal, Slot
```

> If you're doing this in multiple files it can get a bit cumbersome. A nice solution to this is to move the import logic to its own file, e.g. named qt.py in your project root. This module imports the Qt modules (QtCore, QtGui, QtWidgets, etc.) from one of the two libraries, and then you import into your application from there.
> You must remember to add any other PyQt5 modules you use (browser, multimedia, etc.) in both branches of the if block. You can then import Qt5 into your own application with

```python
from .qt import QtGui, QtWidgets, QtCore
```

## QtPy

>Provides a standardized PySide2-like API for PyQt4, PySide, PyQt5... using Qtpy you can control which API to load from your application using the `QT_API` environment variable e.g

```python
import os
os.environ['QT_API'] = 'pyside2'
from qtpy import QtGui, QtWidgets, QtCore  # imports PySide2.
```

 the coding standard for the libraries varies from a mor pythonic code style as both uses Qt and C++ camel case

 while pythonic libraries lean towards use of underscores. In order to avoid confusion, qt derived classes or function I'll follow the qt/C++ coding style, while more pythonic functions to follow PEP8

**UPDATE**

Differences in current versions TL:DR [PyQt6 Vs PySide6](https://www.mfitzp.com/news/pyqt6-vs-pyside6)

1. **Namespaces & Enums**

   > One of the major changes introduced for PyQt6 is    the need to use fully qualified names for enums and    flags. Previously, in both PyQt5 and PySide2 you    could make use of shortcuts -- for example Qt.   DecorationRole, Qt.AlignLeft. In PyQt6 these are now    Qt.ItemDataRole.DisplayRole and Qt.Alignment.   AlignLeft respectively. This change affects all enums    and flag groups in Qt. In PySide6 both long and short    names remain supported.
   > The situation is complicated somewhat by the fact    that PyQt6 and PySide6 use subtly different naming    conventions for flags. In PySide6 (and v5) flags are    grouped under flag objects with the "Flag" suffix,    for example Qt.AlignmentFlag -- the align left flag is Qt.AlignmentFlag.AlignLeft. The same flag group in    PyQt6 is named just "Qt.Alignment". This means that    you can't simply choose long or short form and retain    compatibility between PyQt6 & PySide6.

2. **UI Files**

```python
#in PyQt6: check loadUI
import sys
from PyQt6 import QtWidgets, uic

app = QtWidgets.QApplication(sys.argv)

window = uic.loadUi("mainwindow.ui")
window.show()
app.exec()
```

>The equivalent with PySide6 is one line longer, since you need to create a QUILoader object first. Unfortunately the API of these two interfaces is different too (.load vs .loadUI).

```python
# in PySide6: check load
import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtUiTools import QUiLoader

loader = QUiLoader()

app = QtWidgets.QApplication(sys.argv)
window = loader.load("mainwindow.ui", None)
window.show()
app.exec_()
```
