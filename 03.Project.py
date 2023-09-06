a = float(input("Enter First Number: "))
b = input("Enter Operator (+,-.*,/): ")
c = float(input("Enter Second Number: "))

if b=="+":
    result = a + c
    print (a,b,c,"=",result)
elif b == "-":
    result = a - c
    print (a,b,c,"=",result)
elif b == "*":
    result = a * c
    print (a,b,c,"=",result)
elif b =="/": 
    result = a / c
    print (a,b,c,"=",result)
else: 
    print("Invalid Operator")

