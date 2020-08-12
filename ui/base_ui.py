# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        icon = QIcon()
        icon.addFile(u":/images/images/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.add_new_action = QAction(MainWindow)
        self.add_new_action.setObjectName(u"add_new_action")
        icon1 = QIcon()
        icon1.addFile(u":/images/images/add.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.add_new_action.setIcon(icon1)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.close_action = QAction(MainWindow)
        self.close_action.setObjectName(u"close_action")
        icon2 = QIcon()
        icon2.addFile(u":/images/images/cancel.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_action.setIcon(icon2)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.main_widget = QWidget(self.centralwidget)
        self.main_widget.setObjectName(u"main_widget")
        self.gridLayout_3 = QGridLayout(self.main_widget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.words_widget = QWidget(self.main_widget)
        self.words_widget.setObjectName(u"words_widget")
        self.words_widget.setMaximumSize(QSize(200, 16777215))
        self.gridLayout = QGridLayout(self.words_widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.search_entry = QLineEdit(self.words_widget)
        self.search_entry.setObjectName(u"search_entry")
        self.search_entry.setMaximumSize(QSize(200, 16777215))

        self.gridLayout.addWidget(self.search_entry, 0, 0, 1, 1)

        self.words_listview = QListWidget(self.words_widget)
        self.words_listview.setObjectName(u"words_listview")
        self.words_listview.setMaximumSize(QSize(200, 16777215))

        self.gridLayout.addWidget(self.words_listview, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.words_widget, 1, 0, 1, 1)

        self.definition_widget = QWidget(self.main_widget)
        self.definition_widget.setObjectName(u"definition_widget")
        self.gridLayout_2 = QGridLayout(self.definition_widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.definition_listview = QListWidget(self.definition_widget)
        self.definition_listview.setObjectName(u"definition_listview")

        self.gridLayout_2.addWidget(self.definition_listview, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.definition_widget, 1, 1, 1, 1)


        self.gridLayout_4.addWidget(self.main_widget, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.add_new_action)
        self.menuFile.addAction(self.close_action)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.add_new_action.setText(QCoreApplication.translate("MainWindow", u"Add New Word", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.close_action.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.search_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"search", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

