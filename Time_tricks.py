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



