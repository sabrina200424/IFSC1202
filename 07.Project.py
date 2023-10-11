projectoutputfile = open("07.Project Angles Output.txt", "w")
outputrecord = 0

def ParseDDMMSS (Line):
    degreeposition = Line.find(chr(176)) #finds the degree position
    singlequoteposition = Line.find("'")
    doublequoteposition = Line.find('"')
    degrees = Line[:degreeposition]
    minutes = Line[degreeposition + 1: singlequoteposition]
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
    print(decimaldegrees)
    projectoutputfile.write(str(decimaldegrees) + "\n")
    Line = projectinput.readline()

#projectoutputfile.write(Line)
projectoutputfile.close()

print(outputrecord, "records processed")
