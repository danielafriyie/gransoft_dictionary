"""
Loads dicationary database
"""

import sqlite3 as sq
import os

from exceptions_.exeptions_ import DictDatabaseDoesNotExist


class DictDatabase:
    """Application main database"""

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def __init__(self, path=None, default_path=False):
        if path and default_path:
            raise ValueError('define either \'path\' or \'default\'')
        if not path and not default_path:
            raise ValueError('both path and default_path not defined')

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
        self._cursor.execute('SELECT * FROM entries WHERE word LIKE \'%s\' LIMIT 1' % word)
        return self._cursor.fetchall()

    def add_new_word(self, word, word_type, definition):
        """
        adds new word to the database
        :param word: new word eg: food, book, aeroplane, etc.
        :param word_type: word type eg: noun, adverb, verb, etc.
        :param definition: word definition eg: united -> of unite
        """
        sql = 'INSERT INTO entries VALUES("%s", "%s", "%s")' % (word, word_type, definition)
        self._cursor.execute(sql)
        self._dict_db.commit()

    @property
    def all_words(self):
        self._cursor.execute('SELECT word FROM entries ORDER BY word ASC')
        word_list = [i[0] for i in self._cursor.fetchall()]
        return word_list

    def set_db_path(self, path=None):
        """sets database file path"""
        if path:
            _path = os.path.abspath(path)
            if not os.path.isfile(_path):
                raise DictDatabaseDoesNotExist(f'there\'s no file in << {_path} >>')
            return _path

        default_path = os.path.join(self.BASE_DIR, 'resources/database/_dict.db')
        if not os.path.isfile(default_path):
            raise DictDatabaseDoesNotExist(f'there\'s no file in << {default_path} >>')
        return default_path

    def rollback(self):
        return self._dict_db.rollback()

    def close_db(self):
        """close the database"""
        return self._dict_db.close()


# d = DictDatabase(default_path=True)
# print(d.all_words)
