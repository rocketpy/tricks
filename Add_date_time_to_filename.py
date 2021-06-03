# add Date 
# from datetime import date
from datetime import datetime

date = datetime.now().strftime('%Y_%m_%d')
file_name = f'File {date}.csv

# def get_filename_datetime():
#    return "file-" + str(date.today()) + ".txt"


# add Date and Time
from datetime import datetime

date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
print(f"filename_{date}")


#  add timestamp csv
import time

for val in data:
    now = time.strftime('%d-%m-%Y %H:%M:%S')
    writer.writerow([now, val])
  

# rename xls files from folder 
import os
import re
import datetime


# get xls files
xls_files = [file for file in os.listdir(os.getcwd()) if file.endswith('.xls')]

# get current date
now = datetime.datetime.now()

# change names
for item in xls_files:
    # split name and date part
    name_parts = item.split('.')
    get_date = re.findall('\d+-\d+-\d+', name_parts[0])
    name_string_part = name_parts[0].replace(get_date[0], '')
    # create new name
    new_name = name_string_part + str(now.day) + '-' + str(now.month) + '-' + str(now.year) + '_' + '.xls'
    # rename file
    os.rename(item, new_name)
    
