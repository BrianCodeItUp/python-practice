import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.storylink')
subtexts = soup.select('.subtext')


def create_custom_hn(links, subtexts):
  hn = []
  for idx, item in enumerate(links):
    node = links[idx]
    title = node.getText()
    href = node.get('href', None)
    vote = subtexts[idx].select('.score')
    if (len(vote)):
      points = int(vote[0]
        .getText()
        .replace(' points', '')
      )
      if points > 99:
        hn.append({
          'title': title,
          'href': href,
          'votes': points 
        }) 
  sorted_hn = sorted(hn, key= lambda prop: prop['votes'], reverse=True)
  return sorted_hn


pprint.pprint(create_custom_hn(links, subtexts))

