#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3


class CLI_Prices:
    def __init__(self, db_file):
        self.db_file = db_file

    def run(self):
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()

        c.execute('CREATE TABLE prices (id INTEGER, name TEXT);')

        conn.commit()
        conn.close()


if __name__ == '__main__':
    db_file = 'prices.db'
    cli_prices = CLI_Prices(db_file)
    cli_prices.run()