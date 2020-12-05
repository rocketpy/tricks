import requests
from bs4 import BeautifulSoup


url = 'https://www...'
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'html.parser')
