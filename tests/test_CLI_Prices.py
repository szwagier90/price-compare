#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from src.cli_prices import CLI_Prices

import tempfile
import os


class Test_CLI_Prices(unittest.TestCase):
    def setUp(self):
        self.db_file = tempfile.NamedTemporaryFile(delete=False).name

    def tearDown(self):
        os.remove(self.db_file)

    def test_create_database(self):
        cli_prices = CLI_Prices(db_file=self.db_file)
        cli_prices.run()
        self.assertTrue(os.path.isfile(self.db_file))
        self.assertTrue(is_sqlite3_db(self.db_file))


def is_sqlite3_db(filename):
    from os.path import isfile

    if not isfile(filename):
        return False
    with open(filename, 'rb') as fd:
        header = fd.read(20)
    return header[:16] == 'SQLite format 3\x00'


if __name__ == '__main__':
    unittest.main()
