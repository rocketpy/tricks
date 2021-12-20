# Convert 24 hour time to 12 hour time

from datetime import datetime
data = datetime.strptime("10:30", "%H:%M")
data.strftime("%I:%M %p")
# '10:30 AM'

data = datetime.strptime("22:30", "%H:%M")
data.strftime("%I:%M %p")
# '10:30 PM'


# or
import time

t = time.strftime("%I:%M %p")

# Converting string to datetime
from datetime import datetime

date_time = datetime.strptime('Jul 5 2015  1:22PM', '%b %d %Y %I:%M%p')

# or
from datetime import datetime

date_string = "2012-12-12 10:10:10"
print (datetime.fromisoformat(date_string))
# 2012-12-12 10:10:10


# or
import time

# current time
date_time = time.strftime("%b %d %Y %-I:%M %p")


# Convert a string to date-format
from datetime import datetime

datetime_object = datetime.strptime('5 July 2020','%d %B %Y')
s = datetime_object.strftime("%d/%m/%y")

"""
%a - abbreviated weekday name
%A - full weekday name
%b - abbreviated month name
%B - full month name
%c - preferred date and time representation
%C - century number (the year divided by 100, range 00 to 99)
%d - day of the month (01 to 31)
%D - same as %m/%d/%y %e - day of the month (1 to 31)
%g - like %G, but without the century
%G - 4-digit year corresponding to the ISO week number (see %V)
%h - same as %b %H - hour, using a 24-hour clock (00 to 23)
"""

#  strftime() and strptime() Behavior
#  https://docs.python.org/3.6/library/datetime.html#strftime-and-strptime-behavior

datetime.strptime('1 jul 2009','%d %b %Y')
datetime.datetime(2009, 7, 1, 0, 0)

datetime.strptime('1 Jul 2009','%d %b %Y')
datetime.datetime(2009, 7, 1, 0, 0)

datetime.strptime('jul 21 1996','%b %d %Y')
datetime.datetime(1996, 7, 21, 0, 0)


datetime.strptime('1 July 2009','%d %B %Y')
datetime.datetime(2009, 7, 1, 0, 0)

result = datetime.strptime('1 July 2009','%d %B %Y')
result.strftime('%d/%m/%Y')
# 01/07/2009


from datetime import datetime

datetime_object = datetime.strptime('1 June 2005','%d %B %Y')
print(datetime_object)
# 2005-06-01 00:00:00

print(datetime_object.strftime("%d/%m/%Y"))
# 01/06/2005

