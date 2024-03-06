# deadcode - Find and remove dead code.

# https://pypi.org/project/deadcode/

# pip install deadcode


# Usage

# deadcode .

# Or with command line options:

# deadcode . --exclude=venv,tests --ignore-names=BaseTestCase,*Mixin --ignore-names-in-files=migrations


# The same options can be provided in pyproject.toml settings file:
"""
[tool.deadcode]
exclude = ["venv", "tests"]
ignore-names = ["BaseTestCase", "*Mixin"]
ignore-names-in-files = ["migrations"]
"""


# Command line options:
"""
Option                  	Type	Meaning
--fix		                  Automatically remove detected unused code expressions from the code base.
--exclude	list	          Filenames (or path expressions), which will be completely skipped without being analysed.
--ignore-names	list	    Removes provided list of names from the output. Regexp expressions to match multiple names can also be provided, e.g.
                          *Mixin will match all classes ending with Mixin.
--ignore-names-in-files	  list	Ignores unused names in files, which filenames match provided path expressions.
--ignore-names-if-inherits-from	list	Ignores names of classes, which inherit from provided class names.
--ignore-names-if-decorated-with	list	Ignores names of an expression, which is decorated with one of the provided decorator names.
--ignore-bodies-of	      list	Ignores body of an expression if its name matches any of the provided names.
--ignore-bodies-if-decorated-with	list	Ignores body of an expression if its decorated with one of the provided decorator names.
--ignore-bodies-if-inherits-from	list	Ignores body of a class if it inherits from any of the provided class names.
--ignore-definitions	    list	Ignores definition (including name and body) if a name of an expression matches any of the provided ones.
--ignore-definitions-if-inherits-from	list	Ignores definition (including name and body) of a class if it inherits from any of the provided class names.
--ignore-definitions-if-decorated-with	list	Ignores definition (including name and body) of an expression, which is decorated with any of the provided decorator names.
--no-color	            	Removes colors from the output.
--count	                	Provides the count of the detected unused names instead of printing them all out.
--quiet	                	Does not output anything. Makefile still fails with exit code 1 if unused names are found.
"""


# Ignoring checks with noqa comments
# Inline # noqa comments can be used to ignore deadcode checks. E.g. unused Foo class wont be detected/fixed because # noqa: DC003 comment is used:

class Foo:  # noqa: DC003
    pass
