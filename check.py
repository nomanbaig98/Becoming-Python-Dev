import pprint

import requests
from bs4 import BeautifulSoup

base_url= 'https://news.ycombinator.com/news?p={}'
res = requests.get(base_url.format('99'))
soup = BeautifulSoup(res.text, 'lxml')

print(soup)