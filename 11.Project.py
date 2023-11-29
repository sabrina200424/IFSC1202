

class Student ():  #put all the if statements in the class list
	def __init__(self, firstname, lastname, tnumber):  #make sure to puttwo dashes instead of one
		self.Firstname = firstname
		self.Lastname = lastname
		self.Tnumber = tnumber
		self.Grades = []
	def runningaverage(self):
		total = 0
		count = 0
		for i in range(len(self.Grades)):
			if self.Grades[i].strip() != "":
				total = total + float(self.Grades[i].strip())
				count = count + 1
		if count > 0:
			return total / count
		else: 
			return 0
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


class Studentlist ():

    def __init__(self):
        self.studentlist = []

    def add_student(self, FirstName, LastName, TNumber):
        student = Student(FirstName, LastName, TNumber)
        self.studentlist.append(student)

    def find_student(self, TNumber):
        for i in range(len(self.studentlist)):
              if self.studentlist[i].Tnumber == TNumber:
                   return i
        return -1
         
    def print_student_list(self):
        print("{:>14s}{:>14s}{:>14s}{:>14s}{:>14s}{:>14s}".format("First", "Last", "ID", "Running", "Semester", "Letter"))
        print("{:>14s}{:>14s}{:>14s}{:>14s}{:>14s}{:>14s}".format("Name", "Name", "Number", "Average", "Average", "Grade"))
        print("{:>14s}{:>14s}{:>14s}{:>14s}{:>14s}{:>14s}".format("-"*12, "-"*12, "-"*12, "-"*12, "-"*12, "-"*12))

        for i in range(len(self.studentlist)):
            print ("{:>14s}{:>14s}{:>14s}{:14.2f}{:14.2f}{:>14s}".format(self.studentlist[i].Firstname, self.studentlist[i].Lastname, self.studentlist[i].Tnumber,self.studentlist[i].runningaverage(),self.studentlist[i].totalaverage(),self.studentlist[i].lettergrade()))
        print()
        #print("{} Students in list".format(self.number_of_Students()))
        print()
    
    def add_student_from_file(self,filename):
        projectstudentsfile = open(filename, "r")
        x = projectstudentsfile.readline()
        while x != "":
            y = x.split(",")
            if len(y) == 3:
                self.add_student(y[0], y[1], y[2].strip())
                x = projectstudentsfile.readline()
        projectstudentsfile.close()
    
    def add_scores_from_file(self,filename):
        projectscoresfile = open(filename, "r")
        x = projectscoresfile.readline()
        while x != "":
            y = x.split(",")
            if len(y) == 2:
                TNumber, score = y[0], y[1].strip()
                index = self.find_student(TNumber)
                if index != -1:
                    self.studentlist[index].Grades.append(score)
                x = projectscoresfile.readline()
            
        projectscoresfile.close()
        
mystudentlist = Studentlist()
mystudentlist.add_student_from_file("11.Project Students.txt")
mystudentlist.add_scores_from_file("11.Project Scores.txt")
mystudentlist.print_student_list()
print()