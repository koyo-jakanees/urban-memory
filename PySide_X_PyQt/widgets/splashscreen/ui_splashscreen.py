# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splashscreenumrhVy.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_splashScreen(object):
    def setupUi(self, splashScreen):
        if not splashScreen.objectName():
            splashScreen.setObjectName(u"splashScreen")
        splashScreen.resize(310, 300)
        splashScreen.setStyleSheet(u"#circle_bg{\n"
"  background-color: #282a36;\n"
"  color: #f8f8f2;\n"
"  border-radius: 120px;\n"
"  font: 11pt \"Cascadia Mono PL\";\n"
"}\n"
"#texts{\n"
"  background-color: none;\n"
"  color: #f8f8f2;\n"
"  border-radius: 120px;\n"
"  font: 11pt \"Cascadia Mono PL\";\n"
"}\n"
"#version_lbl{\n"
"  border-radius: 12px;\n"
"  color: rgb(151, 159, 200);\n"
"  background-color: rgb(68,71,90);\n"
"}\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.centralwidget = QWidget(splashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.container = QFrame(self.centralwidget)
        self.container.setObjectName(u"container")
        self.container.setFrameShape(QFrame.NoFrame)
        self.container.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.container)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(20, 20, 20, 20)
        self.circle_bg = QFrame(self.container)
        self.circle_bg.setObjectName(u"circle_bg")
        self.circle_bg.setFrameShape(QFrame.NoFrame)
        self.circle_bg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.circle_bg)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.texts = QFrame(self.circle_bg)
        self.texts.setObjectName(u"texts")
        self.texts.setMaximumSize(QSize(16777215, 160))
        self.texts.setFrameShape(QFrame.StyledPanel)
        self.texts.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.texts)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 0, 0, 0)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.texts)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.texts)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_2, 3, 0, 1, 1)

        self.frame = QFrame(self.texts)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 39))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_2.addWidget(self.frame, 1, 0, 1, 1)

        self.frame_2 = QFrame(self.texts)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setLineWidth(0)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.version_lbl = QLabel(self.frame_2)
        self.version_lbl.setObjectName(u"version_lbl")
        self.version_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.version_lbl, 0, Qt.AlignHCenter)


        self.gridLayout_2.addWidget(self.frame_2, 2, 0, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_2)


        self.verticalLayout_2.addWidget(self.texts)


        self.gridLayout.addWidget(self.circle_bg, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.container)

        splashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(splashScreen)

        QMetaObject.connectSlotsByName(splashScreen)
    # setupUi

    def retranslateUi(self, splashScreen):
        splashScreen.setWindowTitle(QCoreApplication.translate("splashScreen", u"Loading App", None))
        self.label.setText(QCoreApplication.translate("splashScreen", u"Dark SplashScreen", None))
        self.label_2.setText(QCoreApplication.translate("splashScreen", u"loading", None))
        self.version_lbl.setText(QCoreApplication.translate("splashScreen", u"v0.0.1-Beta1", None))
    # retranslateUi

