"""
Gransoft Dictionary
Testing resources.py module
"""

import unittest
import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from resources import DictDatabase
from exceptions_ import DictDatabaseDoesNotExist


class TestResources(unittest.TestCase):

    def setUp(self):
        self.dict_db = DictDatabase(path='_test.db')

    def tearDown(self):
        self.dict_db.rollback()

    def test_resources_path(self):
        with self.assertRaises(DictDatabaseDoesNotExist):
            DictDatabase(path='tests/test.db')

        with self.assertRaises(ValueError):
            DictDatabase(path='test', default_path=True)

        with self.assertRaises(ValueError):
            DictDatabase()

    def test_search_word(self):
        w1, w2 = 'apple', ''

        m1 = self.dict_db.search_word(w1)
        m2 = self.dict_db.search_word(w2)
        self.assertEqual(type(m1), list)
        self.assertEqual(len(m1), 1)
        self.assertEqual(type(m1[0]), tuple)
        self.assertEqual(m1[0][0].lower(), w1)
        self.assertEqual(len(m2), 0)

    def test_add_new_word(self):
        w, w_t, d = 'kokol', 'noun', 'ghanaian poridge'
        self.dict_db.add_new_word(w, w_t, d)
        m = self.dict_db.search_word(w)
        self.assertGreater(len(m), 0)
        self.assertEqual(m[0][0], w)
        self.assertEqual(m[0][1], w_t)
        self.assertEqual(m[0][2], d)


if __name__ == '__main__':
    unittest.main()
