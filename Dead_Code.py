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
