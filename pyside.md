<!-- widgets developed using PySide 2 or 6 -->
# Pyside X PyQt development for rapid GUIs

Since both PySide and PyQt are python bindings to the  Qt C++ framework, generated using Shiboken and Sip respctively; they have subtle differences.
Most common ones would be in the naming of generated classes and modules e.g in imports

```python
from PyQt5.Core import QApplication, Qt
```
```python
from PySide.QtCore import QApplication, Qt
```
One should take keen note on Qt's `signal and slot` calls and naming