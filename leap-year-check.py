def leap_year_check():
    year = int(input("Enter a year to check if it is a leap year: "))

    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("Yes")
    else:
        print("No")


# Checks whether the year is a leap year using a conditional control structure

leap_year_check()
