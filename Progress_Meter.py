# tqdm - Fast, Extensible Progress Meter

# https://pypi.org/project/tqdm/
# tqdm documentation - https://tqdm.github.io/ 

# pip install tqdm


from tqdm import tqdm
for i in tqdm(range(10000)):
    ...


# Usage

# Wrap tqdm() around any iterable:

from tqdm import tqdm
from time import sleep

text = ""

for char in tqdm(["a", "b", "c", "d"]):
    sleep(0.25)
    text = text + char


# trange(i) is a special optimised instance of tqdm(range(i)):
from tqdm import trange

for i in trange(100):
    sleep(0.01)

# Instantiation outside of the loop allows for manual control over tqdm():
pbar = tqdm(["a", "b", "c", "d"])
for char in pbar:
    sleep(0.25)
    pbar.set_description("Processing %s" % char)


#  Manual

with tqdm(total=100) as pbar:
    for i in range(10):
        sleep(0.1)
        pbar.update(10)

"""
If the optional variable total (or an iterable with len()) is provided, predictive stats are displayed.
with is also optional (you can just assign tqdm() to a variable,
but in this case don’t forget to del or close() at the end:
"""

pbar = tqdm(total=100)

for i in range(10):
    sleep(0.1)
    pbar.update(10)
pbar.close()


#  Simple tqdm examples and profiling

# Benchmark
for i in _range(int(1e8)):
    pass

# Basic demo
import tqdm
for i in tqdm.trange(int(1e8)):
    pass

# Some decorations
import tqdm

for i in tqdm.trange(int(1e8), miniters=int(1e6), ascii=True,
                     desc="cool", dynamic_ncols=True):
    pass

# Nested bars

from tqdm import trange

for i in trange(10):
    for j in trange(int(1e7), leave=False, unit_scale=True):
        pass


# Experimental GUI demo

import tqdm
for i in tqdm.tgrange(int(1e8)):
    pass


# Comparison to https://code.google.com/p/python-progressbar/
try:
    from progressbar.progressbar import ProgressBar
except ImportError:
    pass
else:
    for i in ProgressBar()(_range(int(1e8))):
        pass


# Dynamic miniters benchmark
from tqdm import trange
for i in trange(int(1e8), miniters=None, mininterval=0.1, smoothing=0):
    pass


# Fixed miniters benchmark
from tqdm import trange
for i in trange(int(1e8), miniters=4500000, mininterval=0.1, smoothing=0):
    pass


# Demo
import re
from time import sleep
from timeit import timeit

# Simple demo
from tqdm import trange

for _ in trange(16, leave=True):
    sleep(0.1)

# Profiling/overhead tests
stmts = filter(None, re.split(r'\n\s*#.*?\n', __doc__))
for s in stmts:
    print(s.replace('import tqdm\n', ''))
    print(timeit(stmt='try:\n\t_range = xrange'
                 '\nexcept:\n\t_range = range\n' + s, number=1), 'seconds')
