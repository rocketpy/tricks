import os


#  Show current directory
os.getcwd()

#  Check if a file or directory exists
os.path.exists('sample_data')

#  Combining path components
os.path.exists(os.path.join('sample_data', 'README.md'))

#  Create directory
os.mkdir('test_dir')



