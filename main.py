"""
main.py is part of Gransoft Dictionary.

Gransoft Dictionary is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Gransoft Dictionary is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Gransoft Dictionary.  If not, see <https://www.gnu.org/licenses/>.
"""
__appname__ = "GranSoft Dictionary"
__description__ = "English Dictionary Application"
__version__ = "1.0"
__author__ = "Afriyie Daniel"
__email__ = "afriyiedaniel1@outlook.com"
__web__ = "http://danielafriyie.top"
__url__ = "https://github.com/danielafriyie/gransoft_dictionary"
__license__ = "GNU General Public License (GPL) 3.0"
__status__ = "Development"
__maintainer__ = "Afriyie Daniel"
__copyright__ = "Copyright (c) 2020 - Afriyie Daniel"

import sys

from PySide2.QtWidgets import (
    QApplication, QMainWindow, QMessageBox, QWidget, QAbstractItemView
)
from PySide2.QtGui import QIcon, QFont, QColor
from PySide2.QtCore import Qt

from base import Ui_MainWindow, Ui_add_new_word, database


class AddNewWordWindow(Ui_add_new_word, QWidget):
    """add new word window"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle('Add New Word')
        self.cancel_btn.clicked.connect(self.clear_entries)
        self.save_btn.clicked.connect(self.save_btn_callback)

    def clear_entries(self):
        self.word_entry.clear(), self.word_type_entry.clear(), self.word_definition_entry.clear()

    def save_btn_callback(self):
        word = self.word_entry.text()
        word_type = self.word_type_entry.text()
        definition = self.word_definition_entry.toPlainText()

        if not word or not word_type or not definition:
            QMessageBox.about(self, 'Action Required', 'Please fill all the necessary entries!')
            return
        database.add_new_word(word=word, word_type=word_type, definition=definition)
        QMessageBox.about(self, 'Success', '%s added successfully!' % word)
        self.clear_entries()


class GransoftDictionary(Ui_MainWindow, QMainWindow):
    """Gransoft Dictionary Main Window Class"""

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(__appname__ + ' ' + __version__)
        self.set_icon()
        self.populate_words_listview()

        self.entries_label.setText('Total Words: ' + str(database.word_count))

        self.close_action.triggered.connect(self.close_app_callback)
        self.actionAbout.triggered.connect(self.about_window)
        self.add_new_action.triggered.connect(self.add_new_word_callback)
        self.search_entry.textEdited.connect(self.search_word)
        self.words_listview.itemSelectionChanged.connect(self.word_list_view_callback)

    def add_new_word_callback(self):
        self.new_word_window = AddNewWordWindow()
        self.new_word_window.show()

    def set_icon(self):
        icon = QIcon('ui/images/icon.png')
        self.setWindowIcon(icon)

    def about_window(self):
        title = __appname__ + ' ' + __version__
        msg = f'{__appname__}\nVersion: {__version__}\n\n' \
              f'Author: {__author__}\nE-mail: {__email__}\nWeb: {__web__}\nLicense: {__license__}' \
              f'\n\n{__copyright__}'
        QMessageBox.about(self, title, msg)

    def populate_words_listview(self):
        self.words_listview.addItems(database.all_words)

    def search_word(self, word=None, scroll_to_top=True):
        if not word:
            word = self.search_entry.text()
        definition = database.search_word(word=word)

        if not self.search_entry.text():
            self.words_listview.scrollToTop()

        try:
            self.definition_listview.clear()
            i, w, w_t, d = definition[0]
            self.definition_listview.addItem(w)
            self.definition_listview.addItem('\n')
            self.definition_listview.addItem(w_t)
            self.definition_listview.addItem('\n') if w_t else None
            self.definition_listview.addItem(d)

            item_list = (
                self.definition_listview.findItems(w, Qt.MatchExactly)[0],
                self.definition_listview.findItems(w_t, Qt.MatchExactly)[0],
                self.definition_listview.findItems(d, Qt.MatchExactly)[0]
            )
            _w, _t, _d = item_list
            _w.setFont(QFont('Times', 30, QFont.Bold))
            _w.setTextColor(QColor.fromRgb(32, 74, 135))
            _t.setFont(QFont('Helvetica', 15))
            _t.setTextColor(QColor.fromRgb(76, 32, 32))
            _d.setFont(QFont('Times', 15, QFont.Normal))
            _d.setTextColor(QColor.fromRgb(17, 4, 35))

            scroll_pos = self.words_listview.findItems(w, Qt.MatchExactly)[0]
            if scroll_to_top:
                self.words_listview.scrollToItem(scroll_pos, QAbstractItemView.PositionAtTop)
            else:
                self.words_listview.scrollToItem(scroll_pos, QAbstractItemView.ScrollHint.EnsureVisible)

        except IndexError:
            self.definition_listview.clear()

    def word_list_view_callback(self):
        try:
            word = self.words_listview.selectedItems()[0]
            self.search_entry.setText(word.text())
            self.search_word(word=word.text(), scroll_to_top=False)
        except IndexError:
            pass

    def close_app_callback(self):
        database.close_db()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gd = GransoftDictionary()
    gd.show()
    sys.exit(app.exec_())
