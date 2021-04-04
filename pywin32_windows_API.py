#  Win32 (pywin32) extensions, which provides access to many of the Windows APIs from Python.

#  Docs:  http://timgolden.me.uk/pywin32-docs/contents.html
# Git: https://github.com/mhammond/pywin32

# pip install pywin32

# Examples
import pywin32

#  for get Computer Name
name = GetComputerName()

# win32api.FindFiles
some_file = FindFiles(fileSpec)

#Retrieves a list of matching filenames. An interface to the API FindFirstFile/FindNextFile/Find close functions.
# Parameters fileSpec : string

