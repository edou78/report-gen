#!/usr/bin/python

import os,sys,array,platform,string
from report_gen import *

#CLEAR THE SCREEN, DIFFERENT FOR WINDOWS
if string.count(sys.platform,"win") > 0:
	os.system("cls")
elif string.count(sys.platform,"linux") > 0:
	os.system("clear")


report = report_gen()

report.readCSV("students.csv")
report.dispCSV("ALL")

#FOR EVERY ELEMENT IN THE FILE
for elem in range(0,report.countLine()):
	#CHECK IF COMMENT EXISTS
	comm = report.checkComment(elem)
	if comm == 1: #IF NO COMMENT EXISTS
		comment = str(raw_input("Add Comment: "))
		report.addComment(elem,comment)
	elif comm == 0:
		rep = str(raw_input("Comment Exists. Replace?"))
		if (rep == "Y") or (rep == "y"):
			comment = str(raw_input("Add Comment: "))
			report.amendComment(elem,comment)
	else:
		print "error"
report.writeCSV("students.csv")
