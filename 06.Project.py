# w means to copy the code from a file
 
inputfilename = "06.Project Input File.txt"
outputfilename = "06.Project Output File.txt"
inputrecordcount =0
mergefilerecordcount =0

inputfile = open(inputfilename,'r')

outputfile = open(outputfilename,'w')

line =inputfile.readline()

while line != '':
    
    if line == "**Insert File Here**\n":
       mergefilename = "06.Project Merge File.txt"
       mergefile = open(mergefilename, "r")
       mergeline=mergefile.readline()
       while mergeline != "":
           mergefilerecordcount= mergefilerecordcount+1
           outputfile.write(mergeline)
           mergeline = mergefile.readline()
           mergefile.close()
           outputfile.write("\n")
           line=inputfile.readline()
    else:
        inputrecordcount = inputrecordcount+1
        outputfile.write(line)
        line=inputfile.readline()
        
inputfile.close()
outputfile.close()

print("{} input file records".format(inputrecordcount))
print("{} merge file records".format(mergefilerecordcount))
print("{} output file records".format(inputrecordcount+mergefilerecordcount))