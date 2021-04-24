<!-- widgets developed using PySide 2 or 6 and pyqt -->
# Pyside X PyQt development for rapid GUIs

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
