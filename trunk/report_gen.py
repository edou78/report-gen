
class report_gen:
	#CLASS CREATED FOR REPORT GENERATION
	#VARIABLES TO STORE THE CONTENTS OF THE CSV AND THE
	#NUMBER OF LINES, AND THE LINES THAT HAVE COMMENTS
	#PRESENT
	csv_cont = []
	csv_lines=0
	csv_comm = [] 	# IF AN ELEMENT IS 'N' NO COMMENT IS
			# PRESENT, IF A 'C' THEN COMMENTED
	header = ""	
	gender = ""
	#COLUMNS
	#0 - Forename
	#1 - Surname
	#2 - Gender
	#3 - Form
	#4 - Student ID	
	#5 = Comments	

	"Count the number of rows"
	def countLine(self):
		return len(report_gen.csv_cont)
	
	"Read the CSV in, split into lines and elements in the line"	
	def readCSV(self,file_name):
		comm=""
		try:
			csv_file = open(file_name,"r")
		except:
			print "File could not be opened."
			print "Make sure %s is the correct filename" % file_name
			sys.exit()

		for line in csv_file:
			if line[0] != "#":			
				#CHECK LENGTH, CAN TEST FOR COMPLIANT CSV FILE
				#FIND THE LENGTH OF THE LINE, IF COMMENT PRESENT
				#OR NOT PRESENT FILL IN THE CSV_COMM VARIABLE	
				line_split = line.strip().split(',')				
				if (len(line_split) > 6) and (len(line_split) < 5):
					print "CSV FILE HAS INCORRECT NUMBER OF COLUMNS:", len(line_split)
					sys.exit()
				elif len(line_split) == 5:				
					comm = "N"
				elif len(line_split) == 6:
					comm = "C"	
				#else:
				#	print line, len(line_split)				
				report_gen.csv_comm.append(comm)
				report_gen.csv_cont.append(line_split)
				report_gen.csv_lines = report_gen.csv_lines +1
			else:
				#TEST TO SEE IF COMMENT IS ON THE END
				#IF NOT THEN ADD IT
				if report_gen.header.find("Comments") != -1:
					report_gen.header = line.strip()+",Comments\n"
				else:
					report_gen.header = line.strip()			
		csv_file.close()
		
	"WRITE TO THE CSV FILE AGAIN"
	def writeCSV(self,filename):
		try:
			csv_file = open(filename,"w")
		except:
			print "File could not be opened"
			print "Check filename: %s is correct" % filename
			sys.exit()
		
		csv_file.write(report_gen.header)
		#GO THROUGH LINE BY LINE
		for i in range(0,report_gen.csv_lines):
			for j in range(len(report_gen.csv_cont[i])):		
				if j == len(report_gen.csv_cont[i])-1:				
					line = report_gen.csv_cont[i][j]				
				else:
					line = report_gen.csv_cont[i][j]+","	
				csv_file.write(line)
			csv_file.write("\n")
		csv_file.close()	
	
	"CHECK TO SEE IF A COMMENT EXISTS"
	"IF RETURNS:"
	"0 - COMMENT EXISTS"
	"1 - NO COMMENT EXISTS"
	"-1 - ERROR"	
	def checkComment(self,line_no):
		return_val = -2	
		if line_no > report_gen.csv_lines:
			return -1
		else:
			if report_gen.csv_comm[line_no] == "N":
				return_val = 1
			else:
				return_val = 0
		return return_val

	"ADD A COMMENT TO THE LIST USED TO STORE DETAILS FROM THE CSV FILE"				
	def addComment(self,line_no,comment):
		gender = report_gen.csv_cont[line_no][2]			
		#CALL THE PROCESSING FUNCTION
		comment = '''"'''+report_gen.procComm(self,comment,self.gender)+'''"'''
		#ADD THE COMMENT TO THE ARRAY
		val = report_gen.csv_cont[line_no].insert(5,comment)

	def amendComment(self,line_no,comment):				
		#CALL THE PROCESSING FUNCTION
		comment = '''"'''+report_gen.procComm(self,comment,self.gender)+'''"'''
		#ADD THE COMMENT TO THE ARRAY
		report_gen.csv_cont[line_no][5] = comment
	
	"Process the comment, swap he for she if gender is female. Of course do similar if vice-versa"
	def procComm(self,comment,gender):
		#PROCESS THE COMMENT AND CHANGE HE->SHE AND VICE VERSA
		#DEPENDING ON THE GENDER
		if ((gender == "F") or (gender == "f")) and ((comment.find("he") != -1) and (comment.find("she") == -1)):			
			print "Changing to She" 
			print "Old Comment: ", comment
			#REPLACE THE INCORRECT WORD
			print "New Comment: ", comment.replace("he","she")
			comment =comment.replace("he","she")

		elif ((gender == "M") or (gender == "m")) and ((comment.find("she") != -1) and (comment.find(" he") == -1)):		
			print "Changing to He" 
			print "Old Comment: ", comment
			#REPLACE THE INCORRECT WORD
			print "New Comment: ", comment.replace("she","he")
			comment = comment.replace("she","he")

		else:
			print "Comment OK"
			print "Comment: ",comment
		return comment

	"Display a line of the CSV file (dependent on argument)"
	"and also display the number of lines"	
	def dispCSV(self,line):
		ret_val = ""
		if line == "ALL":
			print "Contents:"
			print report_gen.csv_cont
			print "Comments: "
			print report_gen.csv_comm		
			print "Total Number of Lines: ", report_gen.csv_lines
		else:		
			print "Line: ",line
			print "Contents: ",report_gen.csv_cont[line] 
			print "Comments? ",report_gen.csv_comm[line]
			print "Total Number of Lines: ", report_gen.csv_lines

	def dispComm(self,line):
		fore = report_gen.csv_cont[line][0]
		sur = report_gen.csv_cont[line][1]
		gen = report_gen.csv_cont[line][2]
		form = report_gen.csv_cont[line][3]		
		sid = report_gen.csv_cont[line][4]		
	#	comm = report_gen.csv_cont[line][5]
	#	print "%s\t%s\t%s\t%s\t%s\t%s" % (fore,sur,gen,form,sid,comm)
		print "%s\t%s\t%s\t%s\t%s" % (fore,sur,gen,form,sid)

