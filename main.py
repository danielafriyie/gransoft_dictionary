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
__version__ = "1.2.1"
__author__ = "Afriyie Daniel"
__email__ = "afriyiedaniel1@outlook.com"
__web__ = "http://danielafriyie.top"
__url__ = "https://github.com/danielafriyie/gransoft_dictionary"
__license__ = "GNU General Public License (GPL) 3.0"
__status__ = "Development"
__maintainer__ = "Afriyie Daniel"
__copyright__ = "Copyright (c) 2020 - Afriyie Daniel"

try:
    # Include in try/except block if you're also targeting Mac/Linux
    from PySide2.QtWinExtras import QtWin

    appid = 'gransoft.gransoftdictionary'
    QtWin.setCurrentProcessExplicitAppUserModelID(appid)
except ImportError:
    pass

import sys
import os

from PySide2.QtWidgets import (
    QApplication, QMainWindow, QMessageBox, QWidget, QAbstractItemView, QFileDialog
)
from PySide2.QtGui import QIcon, QFont, QColor
from PySide2.QtCore import Qt, QFileInfo

from base import Ui_MainWindow, Ui_add_new_word, database

from logger import logger


class BaseEditPopUpWindow(Ui_add_new_word, QWidget):
    """base edit pop up window"""
    window_title = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle(self.window_title)
        self.set_icon()
        self.cancel_btn.clicked.connect(self.clear_entries)
        self.save_btn.clicked.connect(self.save_btn_callback)

    def clear_entries(self):
        self.word_entry.clear()
        self.word_type_entry.clear()
        self.word_definition_entry.clear()

    def set_icon(self):
        self.setWindowIcon(QIcon('ui/images/icon.png'))

    def save_btn_callback(self):
        pass

    def fill_entries(self, word=None, word_type=None, definition=None):
        """
        populate word, word type and description entries
        :param word:
        :param word_type:
        :param definition:
        :return:
        """
        self.word_entry.setText(word)
        self.word_type_entry.setText(word_type)
        self.word_definition_entry.setText(definition)


class AddNewWordWindow(BaseEditPopUpWindow):
    """add new word window"""

    window_title = 'Add New Word'

    def save_btn_callback(self):
        word = self.word_entry.text()
        word_type = self.word_type_entry.text()
        definition = self.word_definition_entry.toPlainText()

        if not word or not definition:
            QMessageBox.about(self, 'Action Required', 'Please fill all the necessary entries!')
            return
        database.add_new_word(word=word, word_type=word_type, definition=definition)
        QMessageBox.about(self, 'Success', '%s added successfully!' % word)
        self.clear_entries()


class EditWordWindow(BaseEditPopUpWindow):
    """edit word word"""

    window_title = 'Edit Word'

    def save_btn_callback(self):
        word = self.word_entry.text()
        word_type = self.word_type_entry.text()
        definition = self.word_definition_entry.toPlainText()

        if not word or not definition:
            QMessageBox.about(self, 'Action Required', 'Please fill all the necessary entries!')
            return
        database.update_word(word=word, word_type=word_type, definition=definition)
        QMessageBox.about(self, 'Success', '%s updated successfully!' % word)
        self.clear_entries()
        self.close()

        # gd is an object of GransoftDictionary class
        # it's defined at the bottom
        gd.search_word(word=word, scroll_to_top=False)


class GransoftDictionary(Ui_MainWindow, QMainWindow):
    """Gransoft Dictionary Main Window Class"""

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(__appname__ + ' ' + __version__)
        self.set_icon()
        self.populate_words_listview()
        self.total_words_label()
        self.definition_listview.setWordWrap(True)

        self.close_action.triggered.connect(self.close_app_callback)
        self.actionAbout.triggered.connect(self.about_window)
        self.add_new_action.triggered.connect(self.add_new_word_callback)
        self.actionDelete.triggered.connect(self.delete_action_callback)
        self.actionEdit.triggered.connect(self.edit_word_callback)
        self.actionRefresh.triggered.connect(self.refresh_action_callback)
        self.actionEdit.triggered.connect(self.edit_word_callback)
        self.search_entry.textEdited.connect(self.search_word)
        self.words_listview.itemSelectionChanged.connect(self.word_list_view_callback)
        self.actionAbout_Qt.triggered.connect(self.about_qt)
        self.actionBackup.triggered.connect(self.action_backup_callback)
        self.actionLoad.triggered.connect(self.action_load_callback)

        self.add_new_action.setShortcut('Ctrl+N')
        self.actionEdit.setShortcut('Ctrl+E')
        self.actionDelete.setShortcut('Ctrl+D')
        self.actionRefresh.setShortcut('Ctrl+R')
        self.actionBackup.setShortcut('Ctrl+B')
        self.close_action.setShortcut('Ctrl+Q')
        self.actionLoad.setShortcut('Ctrl+L')

    def add_new_word_callback(self):
        self.new_word_window = AddNewWordWindow()
        self.new_word_window.show()

    def edit_word_callback(self):
        try:
            word = self.search_entry.text()
            query_set = database.search_word(word=word)
            if not query_set:
                _w = self.words_listview.selectedItems()[0]
                word = _w.text()
                query_set = database.search_word(word=word)

            w, w_t, d = query_set[0]

            self.edit_word_window = EditWordWindow()
            self.edit_word_window.fill_entries(word=w, word_type=w_t, definition=d)
            self.edit_word_window.show()
        except IndexError as e:
            logger().exception(e)

    def info_message(self, *args, title=None, msg=None):
        arg_list = []
        for _ in args:
            arg_list.append('%s')
        s_arg = ','.join(arg_list)

        if msg:
            msg = msg % args if args else msg

        if not msg:
            msg = 'Do you want to delete ' + s_arg % args

        return QMessageBox.question(
            self,
            title if title else 'Confirm Delete',
            msg,
            QMessageBox.Yes | QMessageBox.No
        )

    def delete_action_callback(self):
        try:
            word = self.words_listview.selectedItems()[0]
            if self.search_entry.text():
                if self.info_message(self.search_entry.text()) is QMessageBox.Yes:
                    database.delete_word(self.search_entry.text())
            elif word.text():
                if self.info_message(word.text()) is QMessageBox.Yes:
                    database.delete_word(word.text())
            self.refresh_action_callback()
        except IndexError as e:
            logger().exception(e)

    def set_icon(self):
        self.setWindowIcon(QIcon('ui/images/icon.png'))

    def total_words_label(self):
        self.entries_label.setText('Total Words: ' + str(database.word_count))

    def about_window(self):
        title = __appname__ + ' ' + __version__
        msg = f'{__appname__}\nVersion: {__version__}\n\n' \
              f'Author: {__author__}\nE-mail: {__email__}\nURL: {__url__}\nLicense: {__license__}' \
              f'\n\n{__copyright__}'
        QMessageBox.about(self, title, msg)

    def about_qt(self):
        QMessageBox.aboutQt(self, 'About Qt - ' + __appname__)

    def populate_words_listview(self):
        self.words_listview.addItems(database.all_words)

    def refresh_action_callback(self):
        self.words_listview.clear()
        self.populate_words_listview()
        self.total_words_label()

    def search_word(self, word=None, scroll_to_top=True):
        if not word:
            word = self.search_entry.text()
        query_set = database.search_word(word=word)

        if not self.search_entry.text():
            self.words_listview.scrollToTop()

        try:
            self.definition_listview.clear()
            w, w_t, d = query_set[0]
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
            _w.setFont(QFont('Times', 20, QFont.Bold))
            _w.setTextColor(QColor.fromRgb(32, 74, 135))
            _t.setFont(QFont('Helvetica', 11, QFont.Normal))
            _t.setTextColor(QColor.fromRgb(17, 4, 35))
            _d.setFont(QFont('Helvetica', 11, QFont.Normal))
            _d.setTextColor(QColor.fromRgb(17, 4, 35))

            scroll_pos = self.words_listview.findItems(w, Qt.MatchExactly)[0]
            if scroll_to_top:
                self.words_listview.scrollToItem(scroll_pos, QAbstractItemView.PositionAtTop)
            else:
                self.words_listview.scrollToItem(scroll_pos, QAbstractItemView.ScrollHint.EnsureVisible)

        except IndexError as e:
            self.definition_listview.clear()
            logger().exception(e)

    def word_list_view_callback(self):
        try:
            word = self.words_listview.selectedItems()[0]
            self.search_entry.setText(word.text())
            self.search_word(word=word.text(), scroll_to_top=False)
        except IndexError as e:
            logger().exception(e)

    def action_backup_callback(self):
        if sys.platform.lower() == 'win32':
            home_dir = os.path.join(os.path.expanduser('~'), 'documents')
        else:
            home_dir = os.path.expanduser('~')

        file_name, _ = QFileDialog.getSaveFileName(
            self, 'Backup Database', home_dir, 'Database file (*.db);; All files(*)'
        )

        if not QFileInfo(file_name).suffix():
            file_name += '.db'

        path, name = QFileInfo(file_name).path(), QFileInfo(file_name).fileName()
        database.backup_db(path=path, backup_name=name)

    def action_load_callback(self):
        if sys.platform.lower() == 'win32':
            home_dir = os.path.join(os.path.expanduser('~'), 'documents')
        else:
            home_dir = os.path.expanduser('~')

        file, _ = QFileDialog.getOpenFileName(
            self, 'Load Database', home_dir, 'Database file (*.db *.sqlite *.sqlite3);; All files(*)',
        )
        database.restore_backup(file)
        self.refresh_action_callback()

    def close_app_callback(self):
        database.close_db()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gd = GransoftDictionary()
    gd.show()
    sys.exit(app.exec_())
