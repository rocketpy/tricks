#  Prospector is a tool to analyse Python code and output information about errors, 
#  potential problems, convention violations and complexity.

# Docs: http://prospector.landscape.io/en/master/
# PyPi:  https://pypi.org/project/prospector/
# pip install prospector

# IMPORTANT !!! Prospector currently supports 12 tools, of which 7 are defaults and 5 are optional extras. !!!
# Supported Tools:  http://prospector.landscape.io/en/master/supported_tools.html

#  For example to install an optional tool such as pyroma:
#  pip install prospector[with_pyroma]

#  Usage:  http://prospector.landscape.io/en/master/usage.html
"""
The simplest way to run prospector is from the project root with no arguments.
It will try to figure everything else out itself and provide sensible defaults:

prospector

# You can specify a path to check:
prospector path/to/my/package

# And you can specify a list of python modules:
prospector module/to/check.py
prospector module/to/check.py other/module/to/check.py something/else.py
"""
