x = int(input("Enter length of time in days: "))
y = 365
z = 7
Year = int(x / y) 
Years = "Years: "
Week = int(x / z)
Weeks = "Weeks: "
Day = int(x % y)
Days = "Days: "
print(Years + str(Year))
print(Weeks + str(Week))
print(Days + str(Day))