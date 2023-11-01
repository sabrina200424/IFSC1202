# Create the array
a = []
# Open the file and read the first line`
numbersfile = open("09.Project Distances.csv")
x = numbersfile.readline().strip()
# While not at end of file
while x != "":
# Split the line into a list
	y = x.split(",")  #they are separated by comma values 
# Convert the values from string to an integer
#	for i in range(len(y)):
#		y[i] = int(y[i])
# Append the list to the two dimensional array
	a.append(y)
# Read the next line
	x = numbersfile.readline().strip()
# Loop through each row in the two dimensional array
for i in range(len(a)):
# Loop though each element in the list
    for j in range(len(a[i])):
# Print each element in the list
        print(
             '{:>10s}'.format(a[i][j]), end=' ')
# End of list - go to next line
    print()



fromcity = input("From City: ")
tocity = input("To City: ")
fromrow = 0
tocolumn = 0

for i in range(len(a)):
    if a[i][0]  == fromcity:  
        fromrow = i 
        break
for i in range(len(a[0])):
    if a[0][i] == tocity:  #moves by column
        tocolumn = i
        break

for i in range(len(a)):
    if fromrow == 0:
        print("Invalid from City")
        break 
for i in range(len(a[0])):
    if tocolumn == 0:
        print("Invalid to City")
        break
#print(fromrow, tocolumn)
print(fromcity, "to", tocity, "-", a[fromrow][tocolumn], "miles")







        #we need to find a, if it's not -1 it's an error
#for j in range(i, 0, -1):  #we put negative 1 because we are looping through it backwards
    #if a[j] == "":
        #start = j
        #break  #we want to put a break in the statement because we are going to loop forwards
#for j in range (i, len(filestring), +1):
    #if filestringlist[j] == "":
        #end = j +1 
        #break
#else:
    #print("Invalid From City")

#for i in range(len(filestringlist)):
    #if filestringlist[i].find(b) != -1:  
        #for j in range(i, 0, -1):  
            #if filestringlist[j] == "":
                #start = j
                #break  
        #for j in range (i, len(filestring), +1):
            #if filestringlist[j] == "":
                #end = j +1 
                #break
        #else:
           # print("Invalid To City")
