#! /usr/bin/python
# -*- coding: utf-8 -*-

import re
import psycopg2

class VVBPgAdapter:
	"""
	Class for simple CRUD and more complex operations with database

 	def save_lines : method for save Skype format messages in db	
	"""
	
	def __init__(self, conn_str):
		self.conn = psycopg2.connect(conn_str)

	# --- SAVE --- #
	def __save_record(self, line, cur):
		if line:
			cur.execute('insert into vvb.records (rectime, nick, message) values (%s, %s, %s)',
				(line[0], line[1], line[2]))

	def save(self, lines):
		cur = self.conn.cursor()
		for line in lines:
			self.__save_record(line, cur)
		self.conn.commit()
		cur.close()

	# --- READ --- #
	def __read(self, query):
		cur = self.conn.cursor()
		cur.execute(query)
		return cur.fetchall()

	def read_all(self):
		return self.__read("select * from vvb.records")

	def read_by_date_range(self, from_date, to_date):
		return self.__read("select * from vvb.records where rectime between '%s' and '%s'" \
			%(from_date, to_date))

	def read_by_nick(self, nick):
		return self.__read("select * from vvb.records where nick = '%s'" % nick)	

	# --- CLOSE --- #
	def close(self):
		self.conn.cursor().close()
		self.conn.close()