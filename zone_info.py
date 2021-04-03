#  zoneinfo — IANA time zone support

# Docs: https://docs.python.org/3/library/zoneinfo.html

from zoneinfo import ZoneInfo
from datetime import datetime, timedelta


dt = datetime(2020, 10, 31, 12, tzinfo=ZoneInfo("America/Los_Angeles"))
print(dt)
# 2020-10-31 12:00:00-07:00

dt.tzname()
# 'PDT'

dt_add = dt + timedelta(days=1)

print(dt_add)
2020-11-01 12:00:00-08:00

dt_add.tzname()
# 'PST'

dt = datetime(2020, 11, 1, 1, tzinfo=ZoneInfo("America/Los_Angeles"))
print(dt)
# 2020-11-01 01:00:00-07:00

print(dt.replace(fold=1))
# 2020-11-01 01:00:00-08:00
      
#  When converting from another time zone, the fold will be set to the correct value:

from datetime import timezone


LOS_ANGELES = ZoneInfo("America/Los_Angeles")
dt_utc = datetime(2020, 11, 1, 8, tzinfo=timezone.utc)

# Before the PDT -> PST transition
print(dt_utc.astimezone(LOS_ANGELES))
# 2020-11-01 01:00:00-07:00

# After the PDT -> PST transition
print((dt_utc + timedelta(hours=1)).astimezone(LOS_ANGELES))
# 2020-11-01 01:00:00-08:00

