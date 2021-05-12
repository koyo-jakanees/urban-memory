# simple text editor GUI

![SimpleSetup](../assets/simpleGuiSet.png)

See source for  code explanation.
> The __`QMainWindow`__ object is the window of your GUI. You define a layout for it and stuff all the components (widgets) into the window, one after the other. We’ve got just two components here: a __`QPushButton`__ and a __`QsciScintilla`__ object. We don’t really need a button, but let’s put it there anyway. The __`QsciScintilla`__ object is what it’s all about. It is the QScintilla editor! Our simple editor won’t need a lexer or other complicated stuff. So the __`QsciLexer`__ and __`QsciAPIs`__ classes are not needed for now (remember from the intro..):
> When building a GUI, I usually start by subclassing the __QMainWindow__ class. First I define the geometry of the window, next I create a central frame: `self.__frm`. This frame will be the parent of all widgets in my GUI. I define a layout for this frame: `self.__lyt` such that all added widgets get positioned vertically, one below the other. As you already know, I create two widgets: the QPushButton and the QsciScintilla editor. I add them to the layout like this

![simpleapiStruct](../assets/apistructSimple.png)

```python
import sys

from PyQt5.Qsci import QsciScintilla
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QApplication, QFrame, QMainWindow,QPushButton,
                             QStyleFactory, QVBoxLayout)


class CustomMainWindow(QMainWindow):
    def __init__(self):
        super(CustomMainWindow, self).__init__()

        # Window setup
        # --------------

        # 1. Define the geometry of the main window
        self.setGeometry(300, 300, 800, 400)
        self.setWindowTitle("QScintilla Test")

        # 2. Create frame and layout
        self.__frm = QFrame(self)
        self.__frm.setStyleSheet("QWidget { background-color: #ffeaeaea }")
        self.__lyt = QVBoxLayout()
        self.__frm.setLayout(self.__lyt)
        self.setCentralWidget(self.__frm)
        self.__myFont = QFont()
        self.__myFont.setPointSize(14)

        # 3. Place a button
        self.__btn = QPushButton("Qsci")
        self.__btn.setFixedWidth(50)
        self.__btn.setFixedHeight(50)
        self.__btn.clicked.connect(self.__btn_action)
        self.__btn.setFont(self.__myFont)
        self.__lyt.addWidget(self.__btn)

        # QScintilla editor setup
        # ------------------------

        # ! Make instance of QsciScintilla class!
        self.__editor = QsciScintilla()
        self.__editor.setText("Hello\n")
        self.__editor.append("world")
        self.__editor.setLexer(None)
        self.__editor.setUtf8(True)  # Set encoding to UTF-8
        self.__editor.setFont(self.__myFont)  # Will be overridden by lexer!

        # ! Add editor to layout !
        self.__lyt.addWidget(self.__editor)

        self.show()

    ''''''

    def __btn_action(self):
        print("Hello World!")

    ''''''


''' End Class '''

if __name__ == '__main__':
    app = QApplication(sys.argv)
    QApplication.setStyle(QStyleFactory.create('Fusion'))
    myGUI = CustomMainWindow()

    sys.exit(app.exec_())

''''''
```
**Edit:** I have removed star imports from this example in favor of explicit imports
From a personal preference and good practice vantage. Most PyQt resources out there in wild internet
also qgis plugins follow this trend, but i prefer minimalist approach of importing only the 
packages and modules you use within an application. This helps understand the packages from 
which a module is inherited and lowers the maintainance cost of an application or porting, migration or 
even  upgrading to a newer package. For instance the Migration from `PyQt4` to `PyQt5` which saw widgets moved to the `QtWidgets` Module from `QtGui`. Unless you had prior knowledge of this, it would be hell migrating your legacy Qt application to recent APIs

## Extending the editor.

some usefull properties to extend the editor.
>Text wrapping automatically breaks the line, such that everything fits in the viewable window. Notice however that wrapped lines don’t increment the line number, and that’s great! Imagine the mess if your text editor starts playing around with line numbers

![wrap mode](../assets/wrapmode.png)
![wrapping visual flags](../assets/wrappingVisualFlags.png)
![start Flag](../assets/startFlag.png)
![indent Flag](../assets/indentOption.png)

Possible errors that you'll encounter
Most of them are self explanatory
by removing the keyword `endFlag` should do the magic
```sh
Traceback (most recent call last):
  File "simpleTextEditor.py", line 82, in <module>
    main()
  File "simpleTextEditor.py", line 75, in main
    myGUI = CustomMainWindow()
  File "simpleTextEditor.py", line 50, in __init__
    self.__editor.setWrapVisualFlags(
TypeError: setWrapVisualFlags(self, QsciScintilla.WrapVisualFlag, startFlag: QsciScintilla.WrapVisualFlag = QsciScintilla.WrapFlagNone, indent: int = 0): 'endFlag' is not a valid keyword argument
```
and due to a typo `QsciScintilla.WrapFlagText` instead of `QsciScintilla.WrapFlagByText`
```sh
Traceback (most recent call last):
  File "simpleTextEditor.py", line 81, in <module>
    main()
  File "simpleTextEditor.py", line 74, in main
    myGUI = CustomMainWindow()
  File "simpleTextEditor.py", line 51, in __init__
    endFlag=QsciScintilla.WrapFlagByBorder, startFlag=QsciScintilla.WrapFlagText)
AttributeError: type object 'QsciScintilla' has no attribute 'WrapFlagText'
```
and
```sh
Traceback (most recent call last):
  File "simpleTextEditor.py", line 82, in <module>
    main()
  File "simpleTextEditor.py", line 75, in main
    myGUI = CustomMainWindow()
  File "simpleTextEditor.py", line 55, in __init__
    self.__editor.setWrapIndentMode(startFlag=QsciScintilla.WrapIndentFixed)
TypeError: setWrapIndentMode() takes no keyword arguments
```
![End of Line options](../assets/EOLOptions.png)
![End of line visibilty](../assets/EOLVisibilty.png)
![Indentation character](../assets/indent_char.png)
![Indentation guides](../assets/indent_guides.png)
![Indentation spaces](../assets/indent_spaces.png)
![Indentation Auto](../assets/Auto_indent.png)
![Caret Visibility](../assets/caret_viz.png)
![Caret foreground](../assets/caret_foreground.png)
![Margin Basics](../assets/margin_basics.png)
![Margin Text](../assets/margin_text.png)
![Margin Type](../assets/margin_type.png)
![Margin Color](../assets/margin_color.png)
![Line Margin](../assets/line_magin.png)
![Line Margin](../assets/line_margin.png)
![Symbol Margin](../assets/symbol_margin.png)
![Creating symbols](../assets/creating_symbols.png)
![Assigning Symbols](../assets/assigning_symbols.png)
![symbols Intermezzo](../assets/symbols_intermezo.png)
![Symbol Warn](../assets/symbol_note.png)
![Displaying symbols](../assets/displaying_symbols.png)
![Symbol setMarginMarkeMask](../assets/symbolMargn_mask.png)
![Symbol upddate](../assets/handles_markers.png)
![Symbol useful functions](../assets/useful_marker_fn.png)