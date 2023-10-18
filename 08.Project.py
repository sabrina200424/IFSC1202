
import requests
response = requests.get('https://www.usconstitution.net/const.txt')
filestring = response.text

filestringlist = filestring.split("\n") #splits the constitution into different lines, row by row
a = input("Enter Search Term: ")
#if a in filestringlist = True

start = 0
end = 1 
while a != "": 
    for i in range(len(filestringlist)):
        if filestringlist[i].find(a) != -1:  #we need to find a, if it's not -1 it's an error
            for j in range(i, 0, -1):  #we put negative 1 because we are looping through it backwards
                if filestringlist[j] == "":
                    start = j
                    break  #we want to put a break in the statement because we are going to loop forwards
            for j in range (i, len(filestring), +1):
                if filestringlist[j] == "":
                    end = j +1 
                    break
            for j in range (start, end):
                print("Line", j, ":", filestringlist[j])
            print()
            i = end
    a = input("Enter Search Term: ")

