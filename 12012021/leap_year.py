# Now write a function to check if a year is leap year or not

def check_leap_year(year):
    # century year divided by 400 is leap year
    if year % 400 == 0:
        print(f"{year} is a leap year")

    # not divided by 100 means not a century year
    # year divided by 4 is a leap year
    elif (year % 4 == 0) and (year % 100 != 0):
        print(f"{year} is a leap year")

    # if not divided by both 400 (century year) and 4 (not century year)
    # year is not leap year
    else:
        print(f"{year} is not a leap year")


check_leap_year(2009)


# shortcut way
def check_leapyear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

check_leap_year(2009)