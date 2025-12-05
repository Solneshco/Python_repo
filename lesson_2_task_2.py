
def is_year_leap_full(year):

    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0