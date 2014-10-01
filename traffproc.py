#!/usr/bin/python
# -*- coding: latin2 -*-

import sys

class traffic:
    def __init__(self, rawStr):
        (self.Down, self.Up) = [ int(x) for x in rawStr.split(":") ]
        self.Total = self.Down + self.Up

def printColumns(columns):
    print "\t".join([str(x) for x in columns])

data = open(sys.argv[1]).readlines()
for monthLine in data:
    (monthHead, monthBody) = monthLine.split("=")
    (traffMark, monthNr, year) = monthHead.split("-")
    monthEntries = [ x.strip() for x in monthBody.split(" ") ]
    monthTotal = traffic(monthEntries[-1].strip("[]"))
    allDaysRaw = monthEntries[:-1]
    allDays = [ traffic(x) for x in allDaysRaw ]
    for dayNr in range(len(allDays)):
        day = allDays[dayNr]
        columns = (year, monthNr, 1+dayNr, day.Down, day.Up, day.Total,)
        printColumns(columns)
    totalDown = sum([ day.Down for day in allDays ])
    totalUp = sum([ day.Up for day in allDays ])
    if (totalDown != monthTotal.Down or totalUp != monthTotal.Up):
        toDump = (totalDown, totalUp, monthTotal.Down, monthTotal.Up,)
        dumpMessage = "Total of %d:%d does not match value at EOL: %d:%d" % toDump
        raise Exception(dumpMessage)

