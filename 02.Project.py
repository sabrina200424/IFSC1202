a = input("Enter side 1: ")
b = input("Enter side 2: ")
c = input("Enter side 3: ")


s = (float(a) + float(b) + float(c)) / 2

#d = float(s) * float(a)
#e = float(s) * float(b)
#f = float(s) * float(c)
#g = s * s
#h = float(g) - float(d)
#i = float(g) - float(e)
#j = float(g) - float(f)

#k = float(h) + float(i) + float(j)

#formula above ended up being wrong, but I'm just keeping code for reference

d = float(s) - float(a)
e = float(s) - float(b)
f = float(s) - float(c)

g = float(s) * float(d) * float(e) * float(f)

import math
area = math.sqrt(g)

Area = "Area :"
print(Area, area)