a = int(input("Enter Start of Range: "))
b = int(input("Enter End of Range: "))
print("Super Special Numbers between", a, "and", b)
for n in range (a, b + 1):
    length = 0
    num = n
    
    while num > 0:
        num = num // 10  
        #print (length)    

        sum = 1
        num = n
    #while num > 0:
        while n in range (1, n + 1):
        sum *= n
        num += sum
        #digit = num % 10
        #sum = sum + digit ** length
        #sum2 = sum // 10
        #num = num // 10
    if sum == n:
        print (sum)
