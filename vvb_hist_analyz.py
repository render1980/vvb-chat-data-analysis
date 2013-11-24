#! /usr/bin/python
# -*- coding: utf-8 -*-

class VVBAnalyz:
	"""
	Class for analyz chat records
	"""
	
	def __init__(self, records):
		self.records = records

	def count(self):
		return len(self.records)