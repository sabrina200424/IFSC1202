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

    #print has to be at the very end of the if statement for the code to not have errors
    #put quotations for the functions
    #elif statement moves down if the first "if" statement is not right
