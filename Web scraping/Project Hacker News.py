# you can write 'robots.txt' at the end of the URL to check info about what is allowed to be scraped
import pprint
import requests
from bs4 import BeautifulSoup

page_still_valid = True
page = 1

while page_still_valid:
    # Concatenate to get new page URL
    base_url = 'https://news.ycombinator.com/news?p=' + str(page)
    # Obtain Request
    res = requests.get(base_url)
    # Check to see if we're on the last page
    if "More" not in res.text:
        break
    # Turn into Soup
    soup = BeautifulSoup(res.text, 'lxml')
    links = soup.select('.storylink')
    subtext = soup.select('.subtext')

    # Add Stories to our list
    def sort_stories_by_votes(hnlist):
        # sorting the stories dictionary by vote in ascending order
        return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


    def create_custom_hn(links, subtext):
        hn = []
        for index, item in enumerate(links):
            title = item.getText()
            # when the link is broken or there is no link present then we use None as a second parameter
            href = item.get('href', None)
            vote = subtext[index].select('.score')
            if len(vote):
                points = int(vote[0].getText().replace(' points', ''))
                if points > 99:
                    hn.append({'title': title, 'link': href, 'votes': points})
        return sort_stories_by_votes(hn)


    # go to next page
    page += 1
    pprint.pprint(create_custom_hn(links, subtext))
