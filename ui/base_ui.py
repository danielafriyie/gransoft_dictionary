# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gransoft_dictionary.ui'
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
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 600)
        icon = QIcon()
        icon.addFile(u":/images/images/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"font-family: \"Times New Roman\", Times, serif;\n"
"font-size: 16px;")
        self.add_new_action = QAction(MainWindow)
        self.add_new_action.setObjectName(u"add_new_action")
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.add_new_action.setIcon(icon1)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.close_action = QAction(MainWindow)
        self.close_action.setObjectName(u"close_action")
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/cancel.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_action.setIcon(icon2)
        self.actionLicense = QAction(MainWindow)
        self.actionLicense.setObjectName(u"actionLicense")
        self.actionEdit = QAction(MainWindow)
        self.actionEdit.setObjectName(u"actionEdit")
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/edit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionEdit.setIcon(icon3)
        self.actionDelete = QAction(MainWindow)
        self.actionDelete.setObjectName(u"actionDelete")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionDelete.setIcon(icon4)
        self.actionRefresh = QAction(MainWindow)
        self.actionRefresh.setObjectName(u"actionRefresh")
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/update.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionRefresh.setIcon(icon5)
        self.actionAbout_Qt = QAction(MainWindow)
        self.actionAbout_Qt.setObjectName(u"actionAbout_Qt")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.words_widget = QWidget(self.centralwidget)
        self.words_widget.setObjectName(u"words_widget")
        self.words_widget.setMaximumSize(QSize(200, 16777215))
        self.words_widget.setStyleSheet(u"margin: 0,0,0,0;\n"
"padding: 0,0,0,0;\n"
"spacing: 0,0,0,0;")
        self.gridLayout = QGridLayout(self.words_widget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.search_entry = QLineEdit(self.words_widget)
        self.search_entry.setObjectName(u"search_entry")
        self.search_entry.setMinimumSize(QSize(0, 30))
        self.search_entry.setMaximumSize(QSize(200, 16777215))
        self.search_entry.setStyleSheet(u"font-family: \"Times New Roman\", Times, serif;\n"
"font-size: 16px;")

        self.gridLayout.addWidget(self.search_entry, 0, 0, 1, 1)

        self.words_listview = QListWidget(self.words_widget)
        self.words_listview.setObjectName(u"words_listview")
        self.words_listview.setMaximumSize(QSize(200, 16777215))
        self.words_listview.setStyleSheet(u"font-family: \"Times New Roman\", Times, serif;\n"
"font-size: 16px;")

        self.gridLayout.addWidget(self.words_listview, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.words_widget, 0, 0, 1, 1)

        self.definition_widget = QWidget(self.centralwidget)
        self.definition_widget.setObjectName(u"definition_widget")
        self.definition_widget.setEnabled(True)
        self.definition_widget.setMaximumSize(QSize(16777212, 16777215))
        self.definition_widget.setStyleSheet(u"margin: 0;\n"
"padding: 0;")
        self.gridLayout_2 = QGridLayout(self.definition_widget)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.definition_listview = QListWidget(self.definition_widget)
        self.definition_listview.setObjectName(u"definition_listview")
        self.definition_listview.setStyleSheet(u"font-family: \"Times New Roman\", Times, serif;\n"
"font-size: 16px;")

        self.gridLayout_2.addWidget(self.definition_listview, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.definition_widget, 0, 1, 1, 1)

        self.entries_label = QLabel(self.centralwidget)
        self.entries_label.setObjectName(u"entries_label")

        self.gridLayout_3.addWidget(self.entries_label, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 24))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.main_toolbar = QToolBar(MainWindow)
        self.main_toolbar.setObjectName(u"main_toolbar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.main_toolbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.add_new_action)
        self.menuFile.addAction(self.actionEdit)
        self.menuFile.addAction(self.actionDelete)
        self.menuFile.addAction(self.actionRefresh)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.close_action)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionAbout_Qt)
        self.main_toolbar.addAction(self.add_new_action)
        self.main_toolbar.addAction(self.actionEdit)
        self.main_toolbar.addAction(self.actionDelete)
        self.main_toolbar.addAction(self.actionRefresh)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.add_new_action.setText(QCoreApplication.translate("MainWindow", u"Add New Word", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.close_action.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.actionLicense.setText(QCoreApplication.translate("MainWindow", u"License", None))
        self.actionEdit.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.actionDelete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.actionRefresh.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.actionAbout_Qt.setText(QCoreApplication.translate("MainWindow", u"About Qt", None))
        self.search_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"search", None))
        self.entries_label.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.main_toolbar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

