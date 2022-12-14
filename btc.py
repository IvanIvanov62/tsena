from bs4 import BeautifulSoup
import requests
import json


def bit():
    b = 0
    URL = "https://garantex.io/"


    def get_html(url, params=None):
        r = requests.get(url, params=params)
        return r


    def get_content(html):
        soup = BeautifulSoup(html, 'html.parser')
        return soup


    def get_items(soup):
        text = ''
        allPricies = soup.findAll('script')
        for item in allPricies:
            pos = item.text.find('{"ask":[')
            if pos != -1:
                posEnd = item.text.find('}]};')
                text = item.text[pos:posEnd + 3]
                break
        items = json.loads(text)
        return items


    def parse(url):
        html = get_html(URL)
        html.encoding = 'utf-8'
        if html.status_code == 200:
            soup = get_content(html.text)
            return soup
        else:
            return 'Error'


    soup = parse(URL)
    if soup == 'Error':
        print('Error')
        exit(0)
    allItems = get_items(soup)
    allItemsAsk = allItems['ask']
    # print(allItems)
    a = 1
    for ask in allItemsAsk:
        if a == 1:
            a += 1
            b = (float((ask['price'])))
    return b
