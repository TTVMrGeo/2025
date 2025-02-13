day = int(input("Enter a day (1-31): "))
if day < 1 or day > 31: print("Error. Day must be between 1 and 31.")

month = int(input("Enter a month (1-12): "))
if month < 1 or month > 12:
    print("Error. Month must be between 1 and 12.")

if month in [2, 4, 6, 9, 11] and day == 31:
    print("Error. Day must be within the month.")

year = int(input("Enter a year (1000 - 9999): "))
if year < 1000 or year > 9999:
    print("Error. Year must have four digits.")