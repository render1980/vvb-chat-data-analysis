#! /usr/bin/python
# -*- coding: utf-8 -*- 

import re
import vvb_hist_parsing
import vvb_hist_db
import vvb_hist_analyz

lines = vvb_hist_parsing.VVBParser().parse('./data/vvb_chat_hist.txt')
pg_adapter = vvb_hist_db.VVBPgAdapter("host=localhost dbname=postgres user=postgres password=postgres port=5432")
# pg_adapter.save(lines)
analyzer = vvb_hist_analyz.VVBAnalyzer(lines, pg_adapter)

# test queries
print "**********************"
print "All messages amount: %s" % analyzer.count()
print "Messages by date range: %s" % analyzer.count_by_date_range('2013-11-01 00:00:00', '2013-11-02 00:00:00')
print "Messages by nick: %s" % analyzer.count_by_nick('mov #029H,MX')
print "**********************"

pg_adapter.close()