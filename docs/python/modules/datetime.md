`datetime`
=

```
import datetime

# DATETIME DATE

# set date, working with YEAR-MONTH-DAY
d = datetime.date(2019, 11, 11)
print(d)
print(datetime.date.today())

tdelta = datetime.timedelta(days=7)
print(datetime.date.today() + tdelta)
date = datetime.date.today() - tdelta
# define week day, "iso"-standart there means start with Monday - 1, not Monday - 0
day_was = date.isoweekday()
print(day_was)

# define days till to my birthday

my_birth_day = datetime.date(2020, 11, 3)
till_bday = my_birth_day - datetime.date.today()
print(till_bday, till_bday.days, till_bday.total_seconds())  # 358 days, 358, 30931200.0

# DATETIME TIME
print("========DATETIME.TIME==========\n")
# set time. working with HOUR-MINUTES-SECONDS-MICROSECONDS
t = datetime.time(9, 52, 6, 5000)
print(t, t.hour, t.minute)

print("========DATETIME.DATETIME==========\n")
# datetime give us access to date(yy, mm ,dd) and time(hh, mm, ss, mm)

dt = datetime.datetime(2019, 11, 11, 20, 56, 45, 1000)
print(dt, dt.date(), dt.time(), dt.year, dt.microsecond)
tdelta = datetime.timedelta(days=7)
print(f"Future week: {dt + tdelta}\n")

dt_today = datetime.datetime.today() # returns current local datetime with timezone None

# .now() - give us the option pass timezone
# if we don't pass time zone - .now() is similar like .today()
dt_now = datetime.datetime.now()
# UTC Greenveech time
dt_utcnow = datetime.datetime.utcnow()
print(dt_today)
print(dt_now)
print(dt_utcnow)

print("USE TIMEZONES\n")
import pytz

dt = datetime.datetime(2019, 11, 11, 20, 15, 46, tzinfo=pytz._UTC())
print(dt)
dt_utc_now = datetime.datetime.now(tz=pytz._UTC())
print(dt_utc_now)

# transform UTC time to our local time
dt_minsk = dt_utcnow.astimezone(pytz.timezone("Europe/Minsk"))
print(dt_minsk)

# for tz in pytz.all_timezones:
#     print(tz)


```
