# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 13:14:46 2018

@author: Naveen Kumar
"""

import requests
from bs4 import BeautifulSoup

for page in range(1, 51):
    r = requests.get(f'http://books.toscrape.com/catalogue/page-{page}.html')
    soup = BeautifulSoup(r.text, "html.parser")
    articles = soup.find_all('article')
    for article in articles:
        a_tag = article.find("h3").find("a")
        title = a_tag["title"]
        price = article.find('p', {"class": 'price_color'}).get_text()
        price = price.replace('Â', '')

        rating_tag = article.find('p')
        rating = rating_tag["class"][1]

        print(f'{title}:{rating}:{price}')
