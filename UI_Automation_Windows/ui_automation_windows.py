#  Do not use 3.7.6 and 3.8.1, comtypes doesn't work in these two versions!!!

# Github: https://github.com/yinkaisheng/Python-UIAutomation-for-Windows
# UI Automation Specification: https://docs.microsoft.com/en-us/windows/win32/winauto/ui-automation-specification

# How to use uiautomation? run 'automation.py -h' 

"""
Understand the arguments of automation.py, and try the following examples:
automation.py -t 0 -n, print current active window's controls, show fullname
automation.py -r -d 1 -t 0, print desktop(the root of control tree) and it's children(top level windows)
"""


# some example
import subprocess
import uiautomation as auto


def test():
    print(auto.GetRootControl())
    subprocess.Popen('notepad.exe')
    # you should find the top level window first, then find children from the top level window
    notepadWindow = auto.WindowControl(searchDepth=1, ClassName='Notepad')
    if not notepadWindow.Exists(3, 1):
        print('Can not find Notepad window')
        exit(0)
    print(notepadWindow)
    notepadWindow.SetTopmost(True)
    # find the first EditControl in notepadWindow
    edit = notepadWindow.EditControl()
    # usually you don't need to catch exceptions
    # but if you meet a COMError exception, put it in a try block
    try:
        # use value pattern to get or set value
        edit.GetValuePattern().SetValue('Hello')# or edit.GetPattern(auto.PatternId.ValuePattern)
    except auto.comtypes.COMError as ex:
        # maybe you don't run python as administrator 
        # or the control doesn't have a implementation for the pattern method(I have no solution for this)
        pass
    edit.SendKeys('{Ctrl}{End}{Enter}World')
    print('current text:', edit.GetValuePattern().Value)
    # find the first TitleBarControl in notepadWindow, 
    # then find the second ButtonControl in TitleBarControl, which is the Maximize button
    notepadWindow.TitleBarControl().ButtonControl(foundIndex=2).Click()
    # find the first button in notepadWindow whose Name is '关闭', the close button
    # the relative depth from Close button to Notepad window is 2
    notepadWindow.ButtonControl(searchDepth=2, Name='关闭').Click()
    # then notepad will popup a window askes you to save or not, press hotkey alt+n not to save
    auto.SendKeys('{Alt}n')

if __name__ == '__main__':
    test()

