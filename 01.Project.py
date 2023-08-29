amount = int(input("Enter length of time in days: "))
x = amount // 365
Years = "Years: "
print(Years , x)
amount = amount - (x * 365)
x = amount // 7
Weeks = "Weeks: "
print(Weeks, x)
y = x * 7
z = amount - y
Days = "Days: "
print("Days:", z)
