

class Student ():  #put all the if statements in the class list
	def __init__(self, firstname, lastname, tnumber, scores):  #make sure to puttwo dashes instead of one
		self.Firstname = firstname
		self.Lastname = lastname
		self.Tnumber = tnumber
		self.Grades = scores
	def runningaverage(self):
		total = 0
		count = 0
		for i in range(len(self.Grades)):
			if self.Grades[i].strip() != "":
				total = total + float(self.Grades[i].strip())
				count = count + 1
		return total / count
	def totalaverage(self):
		total = 0
		for i in range(len(self.Grades)):
			if self.Grades[i].strip() != "":
				total = total + float(self.Grades[i].strip())
		return total / len(self.Grades)
	def lettergrade(self):
		average = self.totalaverage()
		if average >= 90:
			return "A"
		if average >= 80:
			return "B"
		if average >= 70:
			return "C"
		if average >= 60:
			return "D"
		
		return "F"


projectinputfile = open("10.Project Student Scores.txt", "r")
print("{:>12s} {:>12s} {:>12s} {:>12s} {:>12s} {:>12s}".format("First", "Last", "ID", "Running", "Semester","Letter"))
print("{:>12s} {:>12s} {:>12s} {:>12s} {:>12s} {:>12s}".format("Name", "Name", "Number", "Average", "Average","Grade"))
print("{:>12s} {:>12s} {:>12s} {:>12s} {:>12s} {:>12s}".format("-"*12, "-"*12, "-"*12, "-"*12, "-"*12,"-"*12))
x = projectinputfile.readline()

while x != "":
# Split the line into a list
	y = x.split(",")  #they are separated by comma values 
	student = Student (y[0].strip(),y[1].strip(),y[2].strip(),y[3:])
	print("{:>12s} {:>12s} {:>12s} {:>12.2f} {:>12.2f} {:>12s}".format(student.Firstname, student.Lastname, student.Tnumber, student.runningaverage(), student.totalaverage(),student.lettergrade()))
	#the point two value in the number takes the first two numbers
	#the f statements are given out to convert the numbers into floating values
	x = projectinputfile.readline()