# https://pypi.org/project/tqdm/
# pip install tqdm

from tqdm import tqdm
from time import sleep


some_text = ""
for elem in tqdm(["a", "b", "c", "d"]):  # need wrap tqdm() around any iterable
    sleep(0.5)
    some_text = some_text + elem

# or use progress.bar
from time import sleep
from progress.bar import IncrementalBar


some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
bar = IncrementalBar('Left : ', max=len(some_list))

for elem in some_list:
    bar.next()
    time.sleep(0.5)
    
bar.finish()

