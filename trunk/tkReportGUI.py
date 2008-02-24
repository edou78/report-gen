#!/usr/bin/python

import os,sys,array,platform,string
from report_gen import *

from Tkinter import *


class report_gui:

	student = 0
	def __init__(self,master):
		frame = Frame(master)
		frame.pack()
		bwd_lab = self.button_fwd = Button(frame,text="Bwd",command=self.decrementCount)
		bwd_lab.grid(row=0, column=0)
		fwd_lab = self.button_bwd = Button(frame,text="Fwd",command=self.incrementCount)
		fwd_lab.grid(row=0, column=3)
		self.save = Button(frame,text="SAVE",fg="red",command=self.save)	
		self.save.grid(row=0,column=2)	
		status_lab = self.label = Label(frame,relief=SUNKEN,text="A",width=20)
		status_lab.grid(row=10,columnspan=4,sticky=W)
		studID_lab = self.label = Label(frame,text= "Student ID:",width=20,anchor=W)
		studID_lab.grid(row=1,column=0)
		form_lab = self.label = Label(frame,text= "Form:",width=20,anchor=W)
		form_lab.grid(row=2,column=0)
		gender_lab = self.label = Label(frame,text= "Gender:",width=20,anchor=W)
		gender_lab.grid(row=3,column=0)		
		forename_lab = self.label = Label(frame,text= "Forename:",width=20,anchor=W)
		forename_lab.grid(row=4,column=0)
		surname_lab = self.label = Label(frame,text= "Surname:",width=20,anchor=W)
		surname_lab.grid(row=5,column=0)
		comment_lab = self.label = Label(frame,text="Comment:",width=20,anchor=W)
		comment_lab.grid(row=6,column=0)
		proc_no_lab = self.label = Label(frame,text="Processing:",width=20,anchor=W)
		proc_no_lab.grid(row=7,column=0)
		self.of = Label(frame,text="of")
		self.of.grid(row=7,column=2)
		#NOW THE TEXT BOXES
		self.studID = Entry(frame)
		self.studID.grid(row=1,column=1)
		self.form = Entry(frame)
		self.form.grid(row=2,column=1)
		self.gender = Entry(frame)
		self.gender.grid(row=3,column=1)	
		self.forename = Entry(frame)
		self.forename.grid(row=4,column=1)
		self.surname = Entry(frame)
		self.surname.grid(row=5,column=1)
		self.comment = Entry(frame)
		self.comment.grid(row=6,column=1)		
		self.update = Button(frame,text="Update Record",command = self.update)
		self.update.grid(row = 6,column=2)
		self.proc = Entry(frame)
		self.proc.grid(row=7,column=1)
		self.proctot = Entry(frame)
		self.proctot.grid(row=7,column=3)
		
		#CREATE INSTANCE OF THE BACKEND AND READ CSV
		self.report = report_gen()
		self.report.readCSV("students.csv")
		#FIND THE MAX LENGTH
		self.maxline = self.report.countLine()
		self.proc.insert(INSERT,self.student+1)
		#FILL IN THE TEXT BOXES
		self.studID.insert(INSERT,self.report.csv_cont[self.student][4])
		self.form.insert(INSERT,self.report.csv_cont[self.student][3])
		self.forename.insert(INSERT,self.report.csv_cont[self.student][0])
		self.surname.insert(INSERT,self.report.csv_cont[self.student][1])
		self.gender.insert(INSERT,self.report.csv_cont[self.student][2])
		#ADD COMMENT IF IT IS AVAILABLE
		if len(self.report.csv_cont[self.student]) == 6:
			self.comment.insert(INSERT,self.report.csv_cont[self.student][5].strip('''"'''))
		#SET THE CONTENTS OF THE FILE EQUAL TO A LOCAL VARIABLE
	
	def save(self):
		self.report.writeCSV("students.csv")
	def setStudID(self,val):
		self.studID.delete(0,END)
		self.studID.insert(INSERT,val)

	def setForm(self,val):
		self.form.delete(0,END)
		self.form.insert(INSERT,val)

	def setForename(self,val):
		self.forename.delete(0,END)
		self.forename.insert(INSERT,val)

	def setSurname(self,val):
		self.surname.delete(0,END)
		self.surname.insert(INSERT,val)

	def setGender(self,val):
		self.gender.delete(0,END)
		self.gender.insert(INSERT,val)

	def setComment(self,val):
		self.comment.delete(0,END)
		self.comment.insert(INSERT,val)


	def setTot(self):
		self.proctot.insert(0,self.maxline)
	
	def setProc(self,val):
		self.proc.delete(0,END)
		self.proc.insert(INSERT,val)	

	def getComm(self):
		return self.comment.get()

	def update(self):
		#GET THE CONTENTS OF THE FIELD
		comment = self.getComm()
		#IF THERE IS A COMMENT ALREADY, AND IT HAS NOT CHANGED DO NOTHING
		#OTHERWISE, IF THERE IS NO COMMENT, ADD IT
		#IF THE COMMENT HAS CHANGED, UPDATE IT
		if self.report.csv_comm[self.student] == "C":
			if self.report.csv_cont[self.student][5] != comment:
				self.report.amendComment(self.student,comment)
		else:
			self.report.addComment(self.student,comment)
		
	def decrementCount(self):
		self.comment.delete(0,END)		
		if self.student == 0:		
			self.student = self.student
		else:
			self.student = self.student-1
				
		self.setProc(self.student+1)
		self.setStudID(self.report.csv_cont[self.student][4])
		self.setForm(self.report.csv_cont[self.student][3])
		self.setSurname(self.report.csv_cont[self.student][1])
		self.setForename(self.report.csv_cont[self.student][0])
		self.setGender(self.report.csv_cont[self.student][2])
		if self.report.csv_comm[self.student] == "C":
			self.setComment(self.report.csv_cont[self.student][5].strip('''"'''))

	def incrementCount(self):
		self.comment.delete(0,END)		
		if self.report.csv_comm[self.student] == "C":
			self.setComment(self.report.csv_cont[self.student][5].strip('''"'''))
		if self.student == self.maxline-1:
			self.student = self.student
		else:
			self.student = self.student+1
		
		self.setProc(self.student+1)
		self.setStudID(self.report.csv_cont[self.student][4])
		self.setForm(self.report.csv_cont[self.student][3])
		self.setSurname(self.report.csv_cont[self.student][1])
		self.setForename(self.report.csv_cont[self.student][0])
		self.setGender(self.report.csv_cont[self.student][2])



#CLEAR THE SCREEN, DIFFERENT FOR WINDOWS
if string.count(sys.platform,"win") > 0:
	os.system("cls")
elif string.count(sys.platform,"linux") > 0:
	os.system("clear")

#INSTANCE OF THE GUI
root = Tk()
app = report_gui(root)
app.setTot()
	
root.mainloop()
