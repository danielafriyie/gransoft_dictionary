# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_word.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

import image_icons_rc
import new_word_icons_rc

class Ui_add_new_word(object):
    def setupUi(self, add_new_word):
        if not add_new_word.objectName():
            add_new_word.setObjectName(u"add_new_word")
        add_new_word.resize(400, 363)
        add_new_word.setStyleSheet(u"margin: 0;\n"
"padding: 0;\n"
"font-family: \"Times New Roman\", Times, serif;\n"
"font-size: 16px;")
        self.gridLayout_3 = QGridLayout(add_new_word)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.widget = QWidget(add_new_word)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.word_entry = QLineEdit(self.widget)
        self.word_entry.setObjectName(u"word_entry")
        self.word_entry.setMinimumSize(QSize(0, 35))

        self.gridLayout.addWidget(self.word_entry, 0, 0, 1, 1)

        self.word_type_entry = QLineEdit(self.widget)
        self.word_type_entry.setObjectName(u"word_type_entry")
        self.word_type_entry.setMinimumSize(QSize(0, 35))

        self.gridLayout.addWidget(self.word_type_entry, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.widget, 0, 0, 1, 1)

        self.widget_2 = QWidget(add_new_word)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_2 = QGridLayout(self.widget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.word_definition_entry = QTextEdit(self.widget_2)
        self.word_definition_entry.setObjectName(u"word_definition_entry")

        self.gridLayout_2.addWidget(self.word_definition_entry, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.widget_2, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cancel_btn = QPushButton(add_new_word)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setMinimumSize(QSize(0, 35))
        icon = QIcon()
        icon.addFile(u":/icons/images/cancel.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.cancel_btn.setIcon(icon)

        self.horizontalLayout.addWidget(self.cancel_btn)

        self.save_btn = QPushButton(add_new_word)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setMinimumSize(QSize(0, 35))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/apply.png", QSize(), QIcon.Normal, QIcon.Off)
        self.save_btn.setIcon(icon1)

        self.horizontalLayout.addWidget(self.save_btn)


        self.gridLayout_3.addLayout(self.horizontalLayout, 2, 0, 1, 1)


        self.retranslateUi(add_new_word)

        QMetaObject.connectSlotsByName(add_new_word)
    # setupUi

    def retranslateUi(self, add_new_word):
        add_new_word.setWindowTitle(QCoreApplication.translate("add_new_word", u"Form", None))
        self.word_entry.setPlaceholderText(QCoreApplication.translate("add_new_word", u"word", None))
        self.word_type_entry.setPlaceholderText(QCoreApplication.translate("add_new_word", u"word type eg: noun", None))
        self.word_definition_entry.setPlaceholderText(QCoreApplication.translate("add_new_word", u"word definition", None))
        self.cancel_btn.setText(QCoreApplication.translate("add_new_word", u"Cancel", None))
        self.save_btn.setText(QCoreApplication.translate("add_new_word", u"Save", None))
    # retranslateUi

