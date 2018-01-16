#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from src.prices import Comparator
from src.record import Record

class TestPriceComparator(unittest.TestCase):

    def setUp(self):
        self.comparator = Comparator()

    def test_add_no_products_return_empty_list(self):
        self.assertListEqual(self.comparator.show_all(), [])

    def test_add_one_product_return_the_same_one_product(self):
        self.comparator.add_record(Record(1, "Tyskie", "Tesco", 2.80, 1))
        self.assertListEqual(self.comparator.show_all(), [Record(1, "Tyskie", "Tesco", 2.80, 1)])

if __name__ == '__main__':
    unittest.main()
