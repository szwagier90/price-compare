#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import mock

from src.prices import Prices

from src.db.sqlite import SQLiteHandler

class TestPriceComparator(unittest.TestCase):

    def test_new_empty_unnamed_database(self):
        self.db_mock = mock.create_autospec(SQLiteHandler)

        prices = Prices(self.db_mock)

        prices.run()
        self.db_mock.create_database.assert_called_once()


if __name__ == '__main__':
    unittest.main()
