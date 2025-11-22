import datetime as dt

now = dt.datetime.now()


year  = now.year
now.hour
now.minute
now.weekday()
now.month

date_of_birth = dt.datetime(year=2003,month=8,day=26,hour=6,minute=30)
age = now - date_of_birth
age_in_years = age//365
print(age_in_years)
