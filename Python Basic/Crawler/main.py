import requests
from bs4 import BeautifulSoup


def forum_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://thenewboston.com/forum/recent_activity.php?page=' + str(page)
        page_source_code = requests.get(url)
        plain_text = page_source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a', {'class': 'title text-semibold'}):
            Href = link.get('href')
        #   title = link.string
        #   print(Href)
        #   print(title)
            get_single_item_data(Href)
        page += 1

def get_single_item_data(item_url):
    page_source_code = requests.get(item_url)
    plain_text = page_source_code.text
    soup = BeautifulSoup(plain_text)
    for item_name in soup.findAll('a',{'class':'user-name'}):
        print(item_name.string)
    for link in soup.findAll('a'):
        href = link.get('href')
        print(href)

forum_spider(2)