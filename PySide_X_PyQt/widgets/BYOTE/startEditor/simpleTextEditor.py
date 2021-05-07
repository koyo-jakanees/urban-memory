import sys

from PyQt5.Qsci import QsciScintilla
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QApplication, QFrame, QMainWindow, QPushButton,
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
        self.__editor.append("world \n")
        self.__editor.setLexer(None)
        self.__editor.setUtf8(True)  # Set encoding to UTF-8
        self.__editor.setFont(self.__myFont)  # Will be overridden by lexer!
        self.__editor.setWrapMode(QsciScintilla.WrapWord)
        # available wrap modes: 
        # QsciScintilla.WrapNone, WrapWord, WrapCharacter, WrapWhitespace
        self.__editor.setWrapVisualFlags(
            QsciScintilla.WrapFlagByText,
            startFlag=QsciScintilla.WrapFlagByText,
            indent=4)
        # setWrapVisualFlags(endFlag, startFlag, indent)
        # see: readMe
        self.__editor.setWrapIndentMode(QsciScintilla.WrapIndentFixed)
        self.__editor.textChanged.connect(self.text_changed) #signal typing

        # ! Add editor to layout !
        self.__lyt.addWidget(self.__editor)

        self.show()

    ''''''

    def __btn_action(self):
        self.__editor.append('Voila You just clicked the QSci button! \n')
        print("Hello World!")

    def text_changed(self):
        print({self.__editor.text()})
    ''''''
def main():
    app = QApplication(sys.argv)
    QApplication.setStyle(QStyleFactory.create('Fusion'))
    myGUI = CustomMainWindow()

    sys.exit(app.exec_())

''' End Class '''

if __name__ == '__main__':
    main()

''''''