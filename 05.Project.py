a = int(input("Enter Start of Range: "))
b = int(input("Enter End of Range: "))
print("Special Numbers between", a, "and", b)
for n in range (a, b+1):
    length = 0
    num = n
    
    while num > 0:
        num = num // 10 
        length = length + 1       

    sum = 0
    num = n
    while num > 0:
        digit = num % 10
        sum = sum + digit ** length
        num = num // 10
    if sum == n:
        print (sum)
