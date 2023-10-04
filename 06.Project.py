# w means to write a code from a file
# r means to read the code
 
projectinputfile = open("06.Project Input File.txt", "r")
projectoutputfile = open("06.Project Output File.txt", "w")
# set the record to 0 before adding in different numbers 
inputrecord = 0
outputrecord = 0
mergerecord = 0
line = projectinputfile.readline()
while line != "":
    if line == "**Insert Merge File Here**\n":
        # \n means make a new line
        # starts a new line after the insert merge file comment 
        projectmergefile = open("06.Project Merge File.txt","r")
        # open the file first to start adding code in
        mergeline = projectmergefile.readline()
        while mergeline != "":
            projectoutputfile.write(mergeline)
            outputrecord += 1
            mergeline = projectmergefile.readline()
            mergerecord += 1
        projectoutputfile.write("\n")
        projectmergefile.close()
        # Make sure to close the files
    else:
        projectoutputfile.write(line)
        outputrecord += 1
        inputrecord += 1
    line = projectinputfile.readline()
projectinputfile.close()
projectoutputfile.close()
print(inputrecord,"input file record")
print(mergerecord, "merge file record")
print(outputrecord, "output file record")
# output record changes depending on your code