import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.detik.com/terpopuler')
    # print(res.status_code)
soup = BeautifulSoup(res.text, 'html.parser')
populer_area = soup.find(attrs={'class': 'grid-row list-content'})
title = populer_area.findAll(attrs={'class': 'media__title'})
images = populer_area.findAll(attrs={'class': 'media__image'})

for image in images:
    print(image.find('a').find('img')['title'])
