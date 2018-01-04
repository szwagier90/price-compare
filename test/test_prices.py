#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from src.prices import Comparator


class TestPriceComparator(unittest.TestCase):

    def test_new_comparator(self):
        comparator = Comparator()

if __name__ == '__main__':
    unittest.main()
