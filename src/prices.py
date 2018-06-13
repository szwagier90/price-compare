#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3


class Prices:
    def __init__(self):
        pass

    def create_database(self):
        dbfile = '/tmp/test.db'

        conn = sqlite3.connect(dbfile)
        c = conn.cursor()
