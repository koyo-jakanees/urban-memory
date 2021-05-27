# -*-coding:utf-8 -*-
# source tutorial: https://www.mfitzp.com/tutorials/qml-qtquick-python-application/

import sys
from time import strftime, gmtime
import typing
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QObject, QTimer, pyqtSignal


class BackendLogic(QObject):

    updated = pyqtSignal(str, arguments=['time'])

    def __init__(self, parent: typing.Optional['QObject']) -> None:
        super().__init__(parent=parent)

        timer = QTimer()
        timer.setInterval(50)
        timer.timeout.connect(self.update_time)
        timer.start()

    def update_time(self):
        """ Qtimer update"""
        cur_time = strftime('%H:%M:%S', gmtime())
        self.updated.emit(cur_time)


def main():
    """application entry point"""
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    engine.load('main.qml')

    backend = BackendLogic()
    engine.rootObjects()[0].setProperty('backend', backend)
    backend.update_time()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
