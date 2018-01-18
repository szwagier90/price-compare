#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from src.prices import Prices

class Test(unittest.TestCase):

    def test_new_empty_unnamed_database(self):
        prices = Prices()


if __name__ == '__main__':
    unittest.main()
