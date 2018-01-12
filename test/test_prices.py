#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from src.prices import Comparator


class TestPriceComparator(unittest.TestCase):

    def setUp(self):
        self.comparator = Comparator()

    def test_add_no_products_return_empty_list(self):
        self.assertListEqual(self.comparator.show_all(), [])

if __name__ == '__main__':
    unittest.main()
