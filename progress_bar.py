# https://pypi.org/project/tqdm/
# pip install tqdm

from tqdm import tqdm
from time import sleep


some_text = ""
for elem in tqdm(["a", "b", "c", "d"]):  # need wrap tqdm() around any iterable
    sleep(0.5)
    some_text = some_text + elem
