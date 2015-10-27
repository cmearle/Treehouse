import datetime
import pytz

# This code takes a pytz timezone name and converts the local time (central)
# to that timezone

def to_timezone(tz_name):
    local_dt = datetime.datetime.now()
    print(local_dt)
    tz = pytz.timezone(tz_name)
    central_tz = pytz.timezone('US/Central')
    central_dt = central_tz.localize(local_dt)
    print(central_dt)
    print(central_dt.astimezone(tz))

to_timezone('US/Eastern')