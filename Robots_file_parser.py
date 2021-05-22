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

#  Module Installation
"""
On Windows:

C:/> mkdir project && cd project
C:/> python -m venv .venv
C:/> .venv\scripts\activate
(.venv) c:\> python -m pip install --upgrade pip
(.venv) c:\> python -m pip install --upgrade setuptools
(.venv) c:\> python -m pip install robotspy
(.venv) c:\> python -m robots --help
"""


# Usage
"""
The robotspy package can be imported as a module and also exposes an executable, robots, invocable with python -m. If installed globally with pipx, the command robots can be invoked from any folders. The usage examples in the following section use the command robots, but you can also substitute it with python -m robots in a virtual environment.
Execute the Tool

After installing robotspy, you can validate the installation by running the following command:

$ robots --help
usage: robots <robotstxt> <useragent> <path>

Shows whether the given user agent and path combination are allowed or disallowed by the given robots.txt file.

positional arguments:
  robotstxt      robots.txt file path or URL
  useragent      User agent name
  path           Path or URI

optional arguments:
  -h, --help     show this help message and exit
  -v, --version  show program's version number and exit

Examples

The content of http://www.pythontest.net/elsewhere/robots.txt is the following:

# Used by NetworkTestCase in Lib/test/test_robotparser.py

User-agent: Nutch
Disallow: /
Allow: /brian/

User-agent: *
Disallow: /webstats/

To check if the user agent Nutch can fetch the path /brian/ you can execute:

$ robots http://www.pythontest.net/elsewhere/robots.txt Nutch /brian/
user-agent 'Nutch' with path '/brian/': ALLOWED

Or, you can also pass the full URL, http://www.pythontest.net/brian/:

$ robots http://www.pythontest.net/elsewhere/robots.txt Nutch /brian/
user-agent 'Nutch' with url 'http://www.pythontest.net/brian/': ALLOWED

Can user agent Nutch fetch the path /brian?

$ robots http://www.pythontest.net/elsewhere/robots.txt Nutch /brian
user-agent 'Nutch' with path '/brian': DISALLOWED

Or, /?

$ robots http://www.pythontest.net/elsewhere/robots.txt Nutch /
user-agent 'Nutch' with path '/': DISALLOWED

How about user agent Johnny?

$ robots http://www.pythontest.net/elsewhere/robots.txt Johnny /
user-agent 'Johnny' with path '/': ALLOWED

Use the Module in a Project

If you have a virtual environment with the robotspy package installed, you can use the robots module from the Python shell:

(.venv) $ python
>>> import robots
>>> parser = robots.RobotsParser.from_uri('http://www.pythontest.net/elsewhere/robots.txt')
>>> useragent = 'Nutch'
>>> path = '/brian/'
>>> result = parser.can_fetch(useragent, path)
>>> print(f'Can {useragent} fetch {path}? {result}')
Can Nutch fetch /brian/? True

"""

