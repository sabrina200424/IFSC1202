c = int(input("Enter Start of Range: "))
b = int(input("Enter End of Range: "))
print("Prime Numbers between", c, "and", b)
for number in range (c, b + 1):
    if number > 1:
        for i in range(2, number // 2 + 1):
            if (number % i) == 0:
                break 
        else:
            print(number)

# we started off with 2 in the range because 2 is the lowest prime number
#we also have to put a plus 1 because the last digit is smaller than we want since numbers
#start from 0 instead of 1