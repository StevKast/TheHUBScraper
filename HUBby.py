#\31 303889_231f30be-afa7-406f-babf-a50d00af8f8d > div:nth-child(3)

#\31 303889_231f30be-afa7-406f-babf-a50d00af8f8d > div:nth-child(3)

#\34 88841_4653d42a-d11c-4707-a8dc-a657014aaba2 > div:nth-child(3)

#react-app > div > div:nth-child(2) > div > div > div:nth-child(1) > div:nth-child(1) > div > div:nth-child(1) > h1

import requests, bs4

res = requests.get('https://muhub.campuslabs.com/engage/organization/kode2learn')
print(res.raise_for_status)
soup = bs4.BeautifulSoup(res.text, 'html.parser')
name = soup.select('#react-app > div > div:nth-of-type(2) > div > div > div:nth-of-type(4) > div > div > div > div:nth-of-type(1) > span:nth-of-type(1) > h2')

print(len(name))
print(name)

res = requests.get('http://thetataumiami.com/members')
print(res.raise_for_status)
soup = bs4.BeautifulSoup(res.text, 'html.parser')
name = soup.select('body > div.container-fluid > div > div:nth-of-type(1) > h3')

print(len(name))
print(name)
