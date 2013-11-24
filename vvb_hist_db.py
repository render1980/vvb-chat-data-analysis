#! /usr/bin/python
# -*- coding: utf-8 -*-

import re
import psycopg2

class VVBAdapter:
	"""
	Class for simple CRUD and more complex operations with database

 	def save_lines : method for save Skype format messages in db	
	
	"""
	
	def __init__(self, conn_str):
		self.conn = psycopg2.connect(conn_str)

	# HELP METHODS
	def __parse_line(self, line):
		m = re.match(u"^\W(\d+).(\d+).(\d+)\W\s(\d+:\d+:\d+)\W\s([\S\s]+?):\s([\s\S]+)", line)
		if m:
			return ("20" + m.group(3) + "-" + m.group(2) + "-" + m.group(1) + " " + m.group(4),
					m.group(5),
					m.group(6))
	# MODEL LOGIC
	def save_line(self, groups, cur):
		if groups:
			cur.execute('insert into vvb.records (rectime, nick, message) values (%s, %s, %s)', 
					(groups[0], groups[1], groups[2]))
	#else:
	#	err_lines.append(line)

	def save(self, file_name):
		# open postgre connection =>
		cur = self.conn.cursor()
		
		FILE_IN = open(file_name, 'r')
		data = FILE_IN.read()
		FILE_IN.close()
		# normalize text structure
		data = data.replace('\n', ' ').replace('[', '\n[').replace('> \n', '> ').replace(': \n[', ': [')
		lines = data.split('\n')

		for line in lines:
			groups = self.__parse_line(line)
			self.save_line(groups, cur)
		self.conn.commit()
		cur.close()
		self.conn.close()