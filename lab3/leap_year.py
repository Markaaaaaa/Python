def is_leap_year(year):
    if year % 4 == 0:
        return True
    return False


from leap_year import is_leap_year
year = int(input("Enter a year: "))
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
