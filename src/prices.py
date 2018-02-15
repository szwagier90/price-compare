#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Prices:
    def __init__(self, db_handler):
        self.db_handler = db_handler

    def run(self):
        self.db_handler.create_database()
