"""
Gransoft Dictionary.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
__appname__ = "GranSoft Dictionary"
__description__ = "English Dictionary Application"
__version__ = "1.0"
__author__ = "Afriyie Daniel"
__email__ = "afriyiedaniel1@outlook.com"
__web__ = "http://danielafriyie.top"
__license__ = "GNU General Public License (GPL) 3.0"
__status__ = "Development"
__maintainer__ = "Afriyie Daniel"
__copyright__ = "Copyright (c) 2020 - Afriyie Daniel"

from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox, QCompleter, QWidget
from PySide2.QtGui import QIcon

import sys

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
        self.word_completer()
        self.populate_words_listview()
        self.close_action.triggered.connect(self.close_app_callback)
        self.actionAbout.triggered.connect(self.about_window)
        self.add_new_action.triggered.connect(self.add_new_word_callback)

    def add_new_word_callback(self):
        self.new_word_window = AddNewWordWindow()
        self.new_word_window.show()

    def word_completer(self):
        self.search_entry.setCompleter(QCompleter(database.all_words))

    def set_icon(self):
        icon = QIcon('ui/images/icon.png')
        self.setWindowIcon(icon)

    def about_window(self):
        title = __appname__ + ' ' + __version__
        msg = f'{__appname__}\nVersion: {__version__}\n{__description__}\n\n' \
              f'Author: {__author__}\nE-mail: {__email__}\nWeb: {__web__}\nLicense: {__license__}' \
              f'\n\n{__copyright__}'
        QMessageBox.about(self, title, msg)

    def populate_words_listview(self):
        self.words_listview.addItems(database.all_words)

    def close_app_callback(self):
        info = QMessageBox.question(
            self,
            'Confirmation',
            'Do you want to quit GranSoft Dictionary',
            QMessageBox.Yes | QMessageBox.No
        )
        if info is QMessageBox.Yes:
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gd = GransoftDictionary()
    gd.show()
    sys.exit(app.exec_())
