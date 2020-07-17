# remove some symbols from text 

forbidden = ('.','?','!',':',';','-','—',' ',)

some_string = somestring.lower()  # text to lowercase

result = "".join(i for i in somes_tring if i not in forbidden)  # removed all symbols 

res = "".join(i for i in some_string if symbol.isalnum())  # result will contain only letters and numbers
