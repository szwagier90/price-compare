#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

class SQLiteHandler():
	def create_database(self):
		self.db_conn = sqlite3.connect(":memory:")
		c = self.db_conn
		c.execute('''CREATE TABLE kv(key text, value text)''')
		c.execute('''INSERT INTO kv VALUES ('abc', 'def')''')
		self.db_conn.commit()
