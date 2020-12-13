"""
resources.py is part of Gransoft Dictionary.

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

import sqlite3 as sq
import os
import sys
from shutil import copy, rmtree
import re

from exceptions import DictDatabaseDoesNotExist
from logger import logger

from PySide2.QtCore import QFileInfo
from natsort import natsorted


class DictDatabase:
    """Application main database"""

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def __init__(self, path=None, default_path=False):
        if path and default_path:
            raise ValueError('define either \'path\' or \'default_path\'')
        if not path and not default_path:
            raise ValueError('both path or default_path not defined')

        if path:
            self._db_path = self.set_db_path(path=path)
        else:
            self._db_path = self.set_db_path()

        self._dict_db = sq.connect(self._db_path)
        self._cursor = self._dict_db.cursor()

    def search_word(self, word):
        """
        search for word in the database
        :param word: word to look for in the database
        """
        self._cursor.execute(f'SELECT * FROM entries WHERE wordentries LIKE "{word}%" LIMIT 1;')
        query_set = self._cursor.fetchall()
        return query_set

    def add_new_word(self, word, word_type, definition, commit=True):
        """
        adds new word to the database
        :param word: new word eg: food, book, aeroplane, etc.
        :param word_type: word type eg: noun, adverb, verb, etc.
        :param definition: word definition eg: united -> of unite
        :param commit:
        """
        while True:
            try:
                self._cursor.execute('INSERT INTO entries VALUES(?, ?, ?);', (word, word_type, definition))
                break
            except sq.IntegrityError:
                extension = re.findall(r'\s?-\s?[0-9]+', word)
                extension_number = re.findall(r'[0-9]+', ''.join(extension))
                if extension and extension_number:
                    word = word.strip(''.join(extension))
                    number = ''.join(extension_number)
                    word += f' - {int(number) + 1}'
                else:
                    word += ' - 1'
        if commit:
            self._dict_db.commit()

    def delete_word(self, word):
        """
        delete word from database
        :param word: word to delete from database
        :return:
        """
        self._cursor.execute('DELETE FROM entries WHERE wordentries=?;', (word,))
        self._dict_db.commit()

    def update_word(self, word, word_type, definition):
        """
        update word from database
        :param word: word to update
        :param word_type:
        :param definition:
        :return:
        """
        self._cursor.execute(
            'UPDATE entries SET wordtype=?, definition=? WHERE wordentries=?;',
            (word_type, definition, word)
        )
        self._dict_db.commit()

    def truncate(self):
        sql = 'DELETE FROM entries;'
        self._cursor.execute(sql)
        self._dict_db.commit()

    @staticmethod
    def to_integer(s):
        if not isinstance(s, list):
            return ValueError(f'{s} should be a list')
        sups = {
            '\u2070': '0',
            '\xb9': '1',
            '\xb2': '2',
            '\xb3': '3',
            '\u2074': '4',
            '\u2075': '5',
            '\u2076': '6',
            '\u2077': '7',
            '\u2078': '8',
            '\u2079': '9'
        }
        number = ''.join((sups.get(char) for char in s))
        return int(number)

    @staticmethod
    def to_superscript(s):
        """
        Converts string containing numbers to unicode superscript
        :param s: string
        :return: unicode
        """
        sups = {
            u'0': u'\u2070',
            u'1': u'\xb9',
            u'2': u'\xb2',
            u'3': u'\xb3',
            u'4': u'\u2074',
            u'5': u'\u2075',
            u'6': u'\u2076',
            u'7': u'\u2077',
            u'8': u'\u2078',
            u'9': u'\u2079'
        }
        return ''.join(sups.get(char, char) for char in s)

    @property
    def get_db(self):
        return self._dict_db

    @property
    def all_words(self):
        """
        :return: generator object
        """
        self._cursor.execute('SELECT wordentries FROM entries;')
        return natsorted(word[0] for word in self._cursor.fetchall())

    def set_db_path(self, path=None):
        """
        sets database file path
        :param path: path to database file
        """
        if path:
            _path = os.path.abspath(path)
            if not os.path.isfile(_path):
                logger().error(f'there\'s no file in << {_path} >>')
                raise DictDatabaseDoesNotExist(f'there\'s no file in << {_path} >>')
            return _path

        default_path = os.path.join(self.BASE_DIR, 'resources/database/database.db')
        if not os.path.isfile(default_path):
            logger().error(f'there\'s no file in << {default_path} >>')
            raise DictDatabaseDoesNotExist(f'there\'s no file in << {default_path} >>')
        return default_path

    def custom_query(self, sql):
        """
        custom sql query
        :param sql: sql code to execute
        :return: sqlite3.fetchall()
        """
        self._cursor.execute(sql)
        return self._cursor.fetchall()

    def backup_db(self, path=None, backup_name=None):
        """
        takes backup of the database
        :param path: path to save backup
        :param backup_name: saved backup file name
        """
        name = backup_name if backup_name else 'gd_backup.db'
        try:
            if path:
                if not os.path.exists(path):
                    os.mkdir(path)
                self._backup_path = os.path.join(os.path.abspath(path), name)
            else:
                home_path = os.path.expanduser('~')
                save_path = 'documents/' + name
                if sys.platform.lower() == 'win32':
                    self._backup_path = os.path.join(home_path, save_path)
                else:
                    self._backup_path = os.path.join(home_path, name)
        except os.error as e:
            logger().exception(e)

        try:
            backup_conn = sq.connect(self._backup_path)
            self._dict_db.backup(backup_conn)
        except sq.Error as e:
            logger().exception(e)
        finally:
            backup_conn.close()

    def restore_backup(self, path):
        """
        Restore backup data.
        The program copies the backup data to a temporary folder,
        rename it to database.db then copies it back to self._db_path
        then it deletes the temporary folder
        :param path: path to db file
        """
        try:
            sq.connect(path)
            temp_dir = os.path.join(os.path.dirname(self._db_path), 'temp')
            if not os.path.exists(temp_dir):
                os.mkdir(temp_dir)

            db_file = os.path.abspath(path)
            copy(db_file, temp_dir)
            old_temp_fn = os.path.join(temp_dir, QFileInfo(db_file).fileName())
            new_temp_fn = os.path.join(temp_dir, 'database.db')
            os.rename(old_temp_fn, new_temp_fn)
            copy(new_temp_fn, os.path.dirname(self._db_path))
        except sq.Error as e:
            logger().exception(e)
        except os.error as e:
            logger().exception(e)
        finally:
            rmtree(temp_dir)

    @property
    def word_count(self):
        """total count of words in the database"""
        self._cursor.execute('SELECT COUNT(wordentries) FROM entries;')
        return self._cursor.fetchall()[0][0]

    def rollback(self):
        """rollback changes made to the database"""
        self._dict_db.rollback()

    def close_db(self):
        """close the database"""
        self._dict_db.close()
