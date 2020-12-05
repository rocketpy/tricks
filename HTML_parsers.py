import requests
from bs4 import BeautifulSoup


url = 'https://www...'
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'html.parser')  # or, soup = BeautifulSoup(html, 'lxml')
# elems = soup.find_all('section')  # ('section')[1] - return second elem


# or using urllib
import urllib2
from BeautifulSoup import BeautifulSoup


page = urllib2.urlopen('http://www...')
soup = BeautifulSoup(page)
x = soup.body.find('div', attrs={'class' : 'container'}).text


# or using pyquery
from pyquery import PyQuery


html = # here HTML CODE
pq = PyQuery(html)
tag = pq('div#id') # or   tag = pq('div.class')
print(tag.text())
# pq('div#mw-head.noprint')


# HTML DOM Parser
# Official website:  http://thehtmldom.sourceforge.net/
from htmldom import htmldom


# Creating HTML DOM Object
dom = htmldom.HtmlDom()
#or
dom = htmldom.HtmlDom( "http://www.example.com" )
                        
# The above code creates a HtmlDom object.The HtmlDom takes a default parameter,
# the url of the page. If not provided you can create elements dynamically.

dom = dom.createDom("<html></html>')
# or, if you have provided the url then just createDom() call will suffice
dom = dom.createDom()
                    
#  Searching HTML Elements from parse tree:

                    
