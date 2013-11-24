#! /usr/bin/python
# -*- coding: utf-8 -*- 

import re
import vvb_hist_parsing
import vvb_hist_analyz

records = vvb_hist_parsing.VVBParser().parse('./data/vvb_chat_hist.txt')
# print records

analyz = vvb_hist_analyz.VVBAnalyz(records)
print analyz.count()