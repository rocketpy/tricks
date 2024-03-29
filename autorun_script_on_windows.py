# py2exe - Build standalone executables for Windows

# https://pypi.org/project/py2exe/
# Docs - https://www.py2exe.org/
# https://github.com/py2exe/py2exe
# Tutorial - https://www.py2exe.org/index.cgi/Tutorial

# pip install py2exe


# Example
import os
import winreg as reg
            
 
def AddToRegistry():
    # then __file__ will be
    # c:\users\current_user\desktop
    pth = os.path.dirname(os.path.realpath(__file__))
    s_name = "file_name.py"     
    address=os.join(pth, s_name)
    key = HKEY_CURRENT_USER
    key_value = "Software\Microsoft\Windows\CurrentVersion\Run"
    open = reg.OpenKey(key, key_value, 0, reg.KEY_ALL_ACCESS)
    reg.SetValueEx(open, "any_name", 0, reg.REG_SZ,address)
    reg.CloseKey(open)

if __name__=="__main__":
    AddToRegistry()
