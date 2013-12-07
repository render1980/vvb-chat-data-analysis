#! /usr/bin/python
# -*- coding: utf-8 -*-

import vvb_hist_db

class VVBAnalyzer:
	"""
	Class for analyz chat records
	"""
	
	def __init__(self, records, adapter):
		# self.records = records
		self.pg_adapter = adapter

	"""
	Simple
	"""
	def count(self):
		records = self.pg_adapter.read_all()
		return len(records)

	def count_by_date_range(self, from_date, to_date):
		records = self.pg_adapter.read_by_date_range(from_date, to_date)
		return len(records)

	def count_by_nick(self, nick):
		records = self.pg_adapter.read_by_nick(nick)
		return len(records)