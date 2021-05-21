#  robotspy - Robots Exclusion Protocol File Parser

# PyPi: https://pypi.org/project/robotspy/
# Github: https://github.com/andreburgaud/robotspy

# pip install robotspy



"""
Robots Exclusion Standard Parser for Python
The robotspy Python module implements a parser for robots.txt files. The recommended class to use is robots.RobotsParser.

A thin facade robots.RobotFileParser can also be used as a substitute for urllib.robotparser.RobotFileParser,
available in the Python standard library. The class robots.RobotFileParser exposes an API
that is mostly compatible with urllib.robotparser.RobotFileParser.

The main reasons for this rewrite are the following:

It was initially intended to experiment with parsing robots.txt files for a link checker project (not implemented yet).
It is attempting to follow the latest internet draft Robots Exclusion Protocol.
It does not try to be compliant with commonly accepted directives that are not in the current specs such as
request-rate and crawl-delay, but it currently supports sitemaps.
It satisfies the same tests as the Google Robots.txt Parser, except for some custom behaviors specific to Google Robots.
To use the robots command line tool (CLI) in a Docker container, read the following section Docker Image.

To install robotspy globally as a tool on your system with pipx skip to the Global Installation section.

If you are interested in using robotspy in a local Python environment or as a library, skip to section Module Installation.
"""

