# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'anotherWidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import QMetaObject
from PySide2.QtGui import *
from PySide2.QtWidgets import (QHBoxLayout, QListWidget, QPushButton,
                               QSpacerItem, QVBoxLayout, QWidget)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.horizontalLayoutWidget = QWidget(Form)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(9, 10, 381, 271))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_list = QListWidget(self.horizontalLayoutWidget)
        self.main_list.setObjectName(u"main_list")

        self.horizontalLayout.addWidget(self.main_list)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.button_add = QPushButton(self.horizontalLayoutWidget)
        self.button_add.setObjectName(u"button_add")

        self.verticalLayout.addWidget(self.button_add)

        self.button_remove = QPushButton(self.horizontalLayoutWidget)
        self.button_remove.setObjectName(u"button_remove")

        self.verticalLayout.addWidget(self.button_remove)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.button_clear = QPushButton(self.horizontalLayoutWidget)
        self.button_clear.setObjectName(u"button_clear")

        self.verticalLayout.addWidget(self.button_clear)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.button_add.setText(QCoreApplication.translate("Form", u"Add", None))
        self.button_remove.setText(QCoreApplication.translate("Form", u"Remove", None))
        self.button_clear.setText(QCoreApplication.translate("Form", u"Clear", None))
    # retranslateUi

