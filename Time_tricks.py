# Convert 24 hour time to 12 hour time

from datetime import datetime
data = datetime.strptime("10:30", "%H:%M")
data.strftime("%I:%M %p")
# '10:30 AM'

data = datetime.strptime("22:30", "%H:%M")
data.strftime("%I:%M %p")
# '10:30 PM'
