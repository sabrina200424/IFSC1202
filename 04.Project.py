c = int(input("Enter Start of Range: "))
b = int(input("Enter End of Range: "))
print('Prime Numbers: ')
for number in range (c, b + 1):
    if number > 1:
        for i in range(2, number // 2 + 1):
            if (number % i) == 0:
                break 
        else:
            print(number)
