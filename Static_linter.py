# MyPy - Optional static typing for Python

# Docs: https://mypy.readthedocs.io/en/latest/

# python -m pip install mypy

# to run script use:
# python -m mypy test_type.py

# You can teach mypy to detect these kinds of bugs by adding type annotations (also known as type hints).
# For example, you can teach mypy that greeting both accepts and returns a string like so:

def greeting(name: str) -> str:
    return 'Hello ' + name


