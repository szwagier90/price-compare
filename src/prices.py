#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Comparator:
    def __init__(self):
        self.records = []

    def show_all(self):
        return self.records

    def add_record(self, record):
        self.records.append(record)
