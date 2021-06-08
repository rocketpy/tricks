# Docs: https://docs.python.org/3/library/difflib.html

from difflib import SequenceMatcher


with open("file_name_1.txt") as f_1, open("file_name_2.txt") as f_2:
    f_1_data = f_1.read()
    f_2_data = f_2.read()
    similar = SequenceMatcher(None, f_1_data, f_2_data).ratio()
    print(f"Text similar on {similar*100} %")
    
