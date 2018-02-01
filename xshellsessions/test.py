#!/usr/bin/python
# *_* coding: utf-8 *_*

import xlrd
import sys

def readfile(messagefilename, sheetnum):
    "return list of the file rows message"
    message = []
    data = xlrd.open_workbook(messagefilename)
    xlstable = data.sheet_by_index(sheetnum)
    rows = xlstable.nrows
    message.append(rows)
    for row in range(1, rows):
        rowdatas = xlstable.row_values(row)
        if not (len(rowdatas)-1) % 3 == 0:
            print "have err at message.xls row: %d" %row; sys.exit(1)
        message.append({row: rowdatas})
    return message

print readfile('message.xls', 0)
