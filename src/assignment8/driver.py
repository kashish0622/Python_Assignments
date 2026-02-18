from util import dayofweek
x = input("Enter the date (yyyy-mm-dd): ")
name = dayofweek(x)
print("The day on", x, "is {name}")