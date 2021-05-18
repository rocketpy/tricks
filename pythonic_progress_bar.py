# progressist - Minimalist and pythonic progress bar

# PyPI: https://pypi.org/project/progressist/
# Github: https://github.com/pyrates/progressist

# pip install progressist

# Usage
from progressist import ProgressBar

bar = ProgressBar(total=mytotalstuff)
for item in mystuff:
    # do_stuff
    bar.update()
    
