#  pymorphy is - Morphological analyzer !
# https://github.com/kmike/pymorphy2
# pip install pymorphy

#  simple example , open some file with text and use pymorphy2
import re
import pymorphy2


morph = pymorphy2.MorphAnalyzer()

with open('file_name.txt',  encoding='utf-8') as f:
    words = [
        [morph.parse(word)[0].normal_form for word in line.re.findall(r'\w+')]  #  split()
        for line in f
    ]

print(words)

"""
str = 'If this is not possible, for example on a remote CI server !'
print(re.findall(r'\w+', str)) 
"""

"""
with open('file_name.txt',  encoding='utf-8') as file:
    lst = []
    for line in file:
        new_lst = line.split()

        words = []
        for word in new_lst:
            p = morph.parse(word)[0]
            words.append(p.normal_form)
        ls.append(words)
# print(lst)
"""
