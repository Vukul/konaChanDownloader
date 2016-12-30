from bs4 import BeautifulSoup
import random
import urllib.request

safeFilter = False

pages = int(input('How many pages to download: '))
if input('Safe filter? y/n:  ') is 'y':
    safeFilter = True

tagsToUrl = '+' + input('Tags? Press enter for none:  ').replace(' ', '+')

def pictures(max_page):
    print('\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n DOWNLOADING')
    print('------------')
    page = 1
    while page <= max_page:
        url = 'http://konachan.com/post?page='
        url_safe = '&tags=rating%3Asafe'
        url_unsafe = '&tags=%2A'
        url_full = ''
        imageNumber = 0

        if safeFilter:
            url_full = str(url + str(page) + url_safe + tagsToUrl)
        elif safeFilter is False:
            url_full = str(url + str(page) + url_unsafe + tagsToUrl)

        with urllib.request.urlopen(str(url_full)) as response:
            html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        for link in soup.find_all('a', 'directlink'):
            href = 'http:' + link.get('href')
            print(href + '\n')
            full_name = str(imageNumber) + ".jpg"
            imageNumber += 1
            urllib.request.urlretrieve(href, full_name)
        page += 1

pictures(pages)





