# Accept a year and check if it is a leap year.

year = int(input("Enter an year in YYYY format: "))

if year % 100 == 0 and year % 400 == 0:
    print(f"{year} is a leap year")

elif year % 100 != 0 and year % 400 == 0:
    print(f"{year} is a leap year")
    
else:
    print(f"{year} is not a leap year")
