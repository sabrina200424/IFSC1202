amount = int(input("Enter length of time in days: "))
x = amount // 365 
#add in floor divison
years = "Years: "
print(years , x)
amount = amount - (x * 365)
x = amount // 7
weeks = "Weeks: "
print(weeks, x)
y = x * 7
z = amount - y
#put in equation before printing
Days = "Days: "
print("Days:", z)
