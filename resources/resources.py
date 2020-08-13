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

from exceptions_ import DictDatabaseDoesNotExist


class DictDatabase:
    """Application main database"""

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def __init__(self, path=None, default_path=False):
        if path and default_path:
            raise ValueError('define either \'path\' or \'default\'')
        if not path and not default_path:
            raise ValueError('both path or default_path not defined')

        if path:
            _db_path = self.set_db_path(path=path)
        else:
            _db_path = self.set_db_path()

        self._dict_db = sq.connect(_db_path)
        self._dict_db.commit()
        self._cursor = self._dict_db.cursor()

    def search_word(self, word):
        """
        search for word for database
        :param word: word to look for in the database
        """
        self._cursor.execute('SELECT * FROM entries WHERE word LIKE "%s" LIMIT 1;' % word)
        return self._cursor.fetchall()

    def add_new_word(self, word, word_type, definition):
        """
        adds new word to the database
        :param word: new word eg: food, book, aeroplane, etc.
        :param word_type: word type eg: noun, adverb, verb, etc.
        :param definition: word definition eg: united -> of unite
        """
        while True:
            try:
                self._cursor.execute('INSERT INTO entries VALUES(NULL, ?, ?, ?);', (word, word_type, definition))
                break
            except sq.IntegrityError:
                try:
                    match, counter = word[:-3], int(word[-3:][1])
                    word = f'{match}[{counter + 1}]'
                except ValueError:
                    word = f'{word}[2]'
        self._dict_db.commit()

    def delete_word(self, word):
        """
        delete word from database
        :param word: word to delete from database
        :return:
        """
        self._cursor.execute('DELETE FROM entries WHERE word=?;', (word,))
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
            'UPDATE entries SET wordtype=?, definition=? WHERE word=?;',
            (word_type, definition, word)
        )
        self._dict_db.commit()

    @property
    def all_words(self):
        """
        :return: list of words in the database
        """
        self._cursor.execute('SELECT word FROM entries ORDER BY word ASC;')
        word_list = [i[0] for i in self._cursor.fetchall()]
        return word_list

    def set_db_path(self, path=None):
        """
        sets database file path
        :param path: path to database file
        """
        if path:
            _path = os.path.abspath(path)
            if not os.path.isfile(_path):
                raise DictDatabaseDoesNotExist(f'there\'s no file in << {_path} >>')
            return _path

        default_path = os.path.join(self.BASE_DIR, 'resources/database/database.db')
        if not os.path.isfile(default_path):
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

    @property
    def word_count(self):
        """total count of words in the database"""
        self._cursor.execute('SELECT COUNT(word) FROM entries;')
        return self._cursor.fetchall()[0][0]

    def rollback(self):
        """rollback changes made to the database"""
        self._dict_db.rollback()

    def close_db(self):
        """close the database"""
        self._dict_db.close()
