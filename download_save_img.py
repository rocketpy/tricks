import requests


r = requests.get('https://  .png')
with open('file_name.png', 'wb') as f:
    f.write(r.content)
