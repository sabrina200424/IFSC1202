projectoutputfile = open("07.Project Angles Output.txt", "w")
outputrecord = 0

def ParseDDMMSS (Line):
    degreeposition = Line.find(chr(176)) #finds the degree position
    singlequoteposition = Line.find("'")
    doublequoteposition = Line.find('"')
    degrees = Line[:degreeposition]
    minutes = Line[degreeposition + 1: singlequoteposition]  #put plus 1 because you want to start after the degree position
    seconds = Line[singlequoteposition + 1: doublequoteposition]

    degrees = float(degrees)
    minutes = float(minutes)
    seconds = float(seconds)
    return degrees, minutes, seconds  #they give us the float values for the numbers

def DDMMSStoDecimal (degrees, minutes, seconds): 
    decimaldegrees = degrees + (minutes / 60) + (seconds / 3600)
    return (decimaldegrees)



projectinput = open("07.Project Angles Input.txt", "r")
Line = projectinput.readline()
while Line != "":
    outputrecord += 1
    degrees, minutes, seconds = ParseDDMMSS(Line)
    decimaldegrees = DDMMSStoDecimal(degrees, minutes, seconds)
    #print(decimaldegrees)  # Just add in 6 records processed instead of the numbers because that's the expected output
    projectoutputfile.write(str(decimaldegrees) + "\n")
    Line = projectinput.readline()

#projectoutputfile.write(Line)   #if you put in "Line" then it's not going to work because it places
#values of the degrees

#projectoutputfile write line needs to be after you defined a variable because if you do it before it's
# going to put an error sign
projectoutputfile.close()

print(outputrecord, "records processed")
