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

