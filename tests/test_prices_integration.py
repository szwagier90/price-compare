#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from src.prices import Prices

import os


class Test_Prices(unittest.TestCase):

    def test_create_simple_db_add_values_remove_db(self):
        dbfile = '/tmp/test.db'
        self.p = Prices()
        self.p.create_database()
        self.assertTrue(os.path.isfile(dbfile))
        os.remove(dbfile)
        self.assertFalse(os.path.isfile(dbfile))


if __name__ == '__main__':
    unittest.main()
