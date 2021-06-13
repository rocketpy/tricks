# just add this func to your code

def pagination():
    url = 'https:// ... page={}'
    urls = [url.format(str(i)) for i in range(1, 357)]  # range(from 1 page to last page)
    
