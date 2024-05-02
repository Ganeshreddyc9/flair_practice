#  Write a Python program to calculate the number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days

from datetime import date

# f_date = date(2014, 7, 2)
# l_date = date(2014, 7, 11)

# delta = l_date - f_date

# print(delta.days)


def calculate_days(f_date,l_date):

    f_date = date(*f_date)
    l_date = date(*l_date)

    days_difference = (l_date - f_date).days

    return abs(days_difference)

f_date =(2014, 7, 2)

l_date = (2014, 7, 11)

result = calculate_days(f_date,l_date)


print(result)