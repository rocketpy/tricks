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


#  move a file
from distutils.file_util import move_file

move_file("./a", "./b")


#  read a lines
with open("file_name") as f:
    for line in f:
        print(line, end='')
