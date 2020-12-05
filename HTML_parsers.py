import requests
from bs4 import BeautifulSoup


url = 'https://www...'
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'html.parser')


# or using urllib
import urllib2
from BeautifulSoup import BeautifulSoup


page = urllib2.urlopen('http://www...')
soup = BeautifulSoup(page)
x = soup.body.find('div', attrs={'class' : 'container'}).text
