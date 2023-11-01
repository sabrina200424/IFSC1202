a = []
# Open the file and read the first line`
numbersfile = open("Exam Two Properties.csv")
x = numbersfile.readline().strip()
while x != "":
# Split the line into a list
    y = x.split(",")  #they are separated by comma values
    y[4] = float(y[4])
    a.append(y)
    x = numbersfile.readline().strip()
for i in range(len(a)):
    for j in range(len(a[i])):
        print('{:>10s}'.format (float(a[i][j]), end=' '))
    print()

zipcodes = []
count = 0
propertycount = 0


for i in range(len(a)):
    for j in range (len(zipcodes)):
        if a[i][3]  == zipcodes[j][0]:  
            zipcodes [j][1] = zipcodes [j][1] + 1
            propertycount + 1
            break
        else:
            zipcodes.append[0, 1]

average = zipcodes/property

