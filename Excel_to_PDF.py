#  pip install pywin32

from win32com import client
  
# Open Microsoft Excel
excel = client.Dispatch("Excel.Application")
