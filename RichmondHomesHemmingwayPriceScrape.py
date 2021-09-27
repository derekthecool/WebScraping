#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
import re

# # Example scrape from my website dereklomax.com, it extracts items with flow-text class
# URL = 'https://dereklomax.com'
# page = requests.get(URL)
# soup = BeautifulSoup(page.content, 'html.parser')
# flow_text = soup.find_all('p', class_='flow-text')
# for item in flow_text:
#     print(item, end='\n'*2)

URL = 'https://www.richmondamerican.com/utah/salt-lake-city-new-homes/layton/the-park/hemingway/'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
house_price = soup.find_all('h2', class_='base-price')

for item in house_price:
    formatted_price = re.findall("(\$.*)", item.text)
    print(f'{formatted_price[0]}\n')
