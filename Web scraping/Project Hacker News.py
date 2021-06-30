# you can write 'robots.txt' at the end of the URL to check info about what is allowed to be scraped
import pprint

import requests
from bs4 import BeautifulSoup

res = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(res.text, 'lxml')
links = soup.select('.storylink')
votes = soup.select('.score')


def create_custom_hn(links, votes):
    hn = []
    for index, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        points = votes[index].getText()
        print(points)
        hn.append({'title': title, 'link': href})
    return hn


pprint.pprint(create_custom_hn(links, votes))
