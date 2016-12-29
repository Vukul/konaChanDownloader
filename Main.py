import requests
from bs4 import BeautifulSoup
import random
import urllib.request
import os

filter = False
ranPage = False

pages = int(input('How many pages to download: '))
if input('Safe filter? y/n:  ') is 'y':
    filter = True

if input('Random pages? y/n:  ') is 'y':
    ranPage = True

def pictures(max_page):
    os.system('cls')
    print('DOWNLOADING')
    print('------------')
    page = 1
    while page <= max_page:
        url = 'http://konachan.com/post?page='
        url_safe = '&tags=rating%3Asafe'
        url_unsafe = '&tags=%2A'

        if filter:
            if ranPage:
                source_code = requests.get(url + str(random.randrange(1, 6331)) + url_safe)
            else:
                source_code = requests.get(url + str(page) + url_safe)
        elif filter is False:
            if ranPage:
                source_code = requests.get(url + str(random.randrange(1, 6331)) + url_unsafe)
            else:
                source_code = requests.get(url + str(page) + url_unsafe)

        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')
        for link in soup.find_all('a', 'directlink'):
            href = 'http:' + link.get('href')
            print(href + '\n')
            name = random.randrange(0, 10000)
            full_name = str(name) + ".jpg"
            urllib.request.urlretrieve(href, full_name)
        page += 1

pictures(pages)




