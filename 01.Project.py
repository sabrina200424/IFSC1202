x = int(input("Enter length of time in years: "))
y = 365
z = 52
Year = int(x / y) 
Years = "Years: "
Month = int(x % z)
Months = "Months: "
Day = int(x % y)
Days = "Days: "
print(Years + str(Year))
print(Months + str(Month))
print(Days + str(Day))