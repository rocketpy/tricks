import os


#  Show current directory
os.getcwd()

#  Check if a file or directory exists
os.path.exists('sample_data')

if not os.path.exists('test_dir'):
    os.mkdir('test_dir')

#  Combining path components
os.path.exists(os.path.join('sample_data', 'README.md'))

#  Create directory
os.mkdir('test_dir')

#  Showing the contents of the directory
os.listdir('sample_data')

#  Find all CSV files in a directory
from glob import globlist(glob(os.path.join('sample_data', '*.csv')))

#  Moving files
import shutilfor file in list(glob(os.path.join('sample_data', '*.csv'))):
    shutil.move(file, 'test_dir')
    
    for file in list(glob(os.path.join('test_dir', '*.csv'))):
    os.rename(
        file,
        os.path.join(
            'sample_data',
            os.path.basename(file)
    ))
    
#  Copying files
shutil.copy(
    os.path.join('sample_data', 'README.md'),
    os.path.join('test_dir')
)

#  Deleting files and folders
os.remove(os.path.join('test_dir', 'README(1).md'))
# or
os.rmdir(os.path.join('test_dir', 'level_1', 'level_2', 'level_3'))


# Source: https://habr.com/ru/company/selectel/blog/547290/
