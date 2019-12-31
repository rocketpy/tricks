# for python 3.4+ 
import pathlib
 
    
path = pathlib.Path('my_music.mp3')
print(path.exists()) 
# True
print(path.is_file()) 
# True


# using module OS , for any python version
import os.path
 
    
check_file = os.path.exists('storage/music.mp3') 
# True
print(os.path.exists('some_name.txt')) 
# False
 
# checking is some directory exist 
os.path.exists('storage') 
# True

# using os.path.isfile()  for check is file or not
 
os.path.isfile('storage/music.mp3') 
# True
os.path.isfile('some_name.txt') 
# False
os.path.isfile('storage')
# False, directory exist but it's not a file !!!
