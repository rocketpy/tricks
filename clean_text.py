# remove some symbols from text 

forbidden = ('.', '?', '!', ':', ';', '-', '—', ' ',)

some_string = somestring.lower()  # text to lowercase

result = "".join(i for i in somes_tring if i not in forbidden)  # removed all symbols 

res = "".join(i for i in some_string if symbol.isalnum())  # result will contain only letters and numbers


# other case
import pandas as pd
import string

data = pd.read_csv(file_name_csv, encoding='UTF-8')
#  here need use loop for , for column !!!

result = set(string.printable)  # 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ 
some_word = 'some bad words'
''.join(filter(lambda x: x in result, some_word))
