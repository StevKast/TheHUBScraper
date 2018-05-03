#\31 303889_231f30be-afa7-406f-babf-a50d00af8f8d > div:nth-child(3)
#\34 88841_4653d42a-d11c-4707-a8dc-a657014aaba2 > div:nth-child(3)

import urllib2
from bs4 import BeautifulSoup

pageUrl = 'https://muhub.campuslabs.com/engage/organization/kode2learn'

page = urllib2.urlopen(pageUrl)

soup = BeautifulSoup(page, ‘html.parser’)

presBox = soup.find(‘h1’, attrs={‘class’: ‘name’})
