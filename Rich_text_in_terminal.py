#  Rich is a Python library for rich text and beautiful formatting in the terminal.

# PyPi:  https://pypi.org/project/rich/9.13.0/
# Github:  https://github.com/willmcgugan/rich

# pip install rich

# to run the following to test Rich output on your terminal:
# python -m rich

from rich import print

print("Hello, [bold magenta]World[/bold magenta]!", ":vampire:", locals())


#  Using the Console
from rich.console import Console

console = Console()
console.print("Hello", "World!")
console.print("Hello", "World!", style="bold red")
