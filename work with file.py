#  read a file
with open("file_name", encoding="utf-8") as f:  # use file_name or path to file !!!
    cont = f.read()
print(type(contt))

# read , binary mode !
with open("file_name", "rb") as f:
    cont = f.read()
print(type(contt))

#  write a file
some_content = "Hello world !"
with open("new_file.txt", "w") as file:
    file.write(file_content)
    
#  copy a file
from distutils.file_util import copy_file

copy_file("a", "b")

# copying Files and Folders
import shutil, os

os.chdir('C:\\')
shutil.copy('C:\\spam.txt', 'C:\\del')
## 'C:\\del\\spam.txt'

shutil.copy('eg.txt', 'C:\\del\\eg2.txt')
## 'C:\\del\\eg2.txt'

# copying all files tree
import shutil, os

os.chdir('C:\\')

shutil.copytree('C:\\bac', 'C:\\bac_up')
## 'C:\\bac_up'

# moving and renaming files or dirs
import shutil

shutil.move('C:\\bac.txt', 'C:\\eg')
## 'C:\\eg\\bac.txt'
# or
shutil.move('C:\\bac.txt', 'C:\\eg\\new_bac.txt')
# or
shutil.move('C:\\bac.txt', 'C:\\eg')

#  move a file
from distutils.file_util import move_file

move_file("./a", "./b")


#  read a lines
with open("file_name") as f:
    for line in f:
        print(line, end='')

        
# working with path
from pathlib import Path
 
root = Path('make_sub_folder')
print(root)
 
path = root / 'happy_user'  # make path as absolute !
 
print(path.resolve())


#  make a loop for directory with a many files ( CSV )
import os

from os.path import join
my_csv=[]
for root, dirs, files in os.walk('data2test'):
    my_csv.extend([join(root, file) for file in files if file.endswith('csv')]) 
    dirs.clear()
 

for file in my_csv:
    pass
