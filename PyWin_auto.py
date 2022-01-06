# Setup

run pip install -U pywinauto (dependencies will be installed automatically)


from pywinauto.application import Application


app = Application().start("notepad.exe")

app.UntitledNotepad.menu_select("Help->About Notepad")
app.AboutNotepad.OK.click()
app.UntitledNotepad.Edit.type_keys("pywinauto Works!", with_spaces = True)
