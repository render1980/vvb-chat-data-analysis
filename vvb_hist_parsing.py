#! /usr/bin/python
# -*- coding: utf-8 -*-

import re
	
class VVBParser:
	"""
	Class for parsing unstructured text with messages of Skype chat format 
	"""
	
	def __init__(self):
		self.records = []
		err_lines = []

	# help methods
	def __parse_line(self, line):
		m = re.match(u"^\W(\d+).(\d+).(\d+)\W\s(\d+:\d+:\d+)\W\s([\S\s]+?):\s([\s\S]+)", line)
		if m:
			return ("20" + m.group(3) + "-" + m.group(2) + "-" + m.group(1) + " " + m.group(4),
					m.group(5), m.group(6))

	# model logic
	def __save_line(self, groups):
		if groups:
			#print (groups[0] + " | " + groups[1] + " | " + groups[2] + "\n")
			self.records.append((groups[0], groups[1], groups[2]))

	def parse(self, file_name):
		FILE_IN = open(file_name, 'r')
		data = FILE_IN.read()
		FILE_IN.close()
		# normalize text structure
		data = data.replace('\n', ' ').replace('[', '\n[').replace('> \n', '> ').replace(': \n[', ': [')
		lines = data.split('\n')
		for line in lines:
			groups = self.__parse_line(line)
			self.__save_line(groups)
		return self.records

# Main workflow #
lines = VVBParser().parse('./data/vvb_chat_hist.txt')
