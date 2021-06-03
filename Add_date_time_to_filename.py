


# add Date and Time
from datetime import datetime

date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
print(f"filename_{date}")


#  add timestamp csv
import time

for val in data:
    now = time.strftime('%d-%m-%Y %H:%M:%S')
    writer.writerow([now, val])
    
