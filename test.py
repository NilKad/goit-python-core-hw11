from datetime import datetime


# date1 = datetime.datetime(year="1972", month="11", day="11")

date_now = datetime.now().date()
print(date_now)

# date1 = datetime(1972, 11, 11).date().replace(year=date_now.year)
date1 = datetime(1972, 1, 1).date().replace(year=date_now.year)
print(date1)

delta_date = (date1 - date_now).days

if delta_date < 0:
    delta_date = (date1.replace(year=date_now.year + 1) - date_now).days
# else:

# p = delta_date.timedelta(day)
print(f"delta_date: {delta_date}")

# print(f"diff: {date_now - date1}")


a = None
if a:
    print("True")
else:
    print("False")


book = dict()

book['a'] = 1
book['b'] = 2

print(book)
