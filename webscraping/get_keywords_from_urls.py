from bs4 import BeautifulSoup
import requests

with open('urls.txt') as f:
    for url in f.readlines():
        url = url.strip()
        req  = requests.get(url)
        soup = BeautifulSoup(req.text, "html.parser")
        print(url)
        print(soup.find('meta', {'name': 'keywords'})['content'])
        print('\n')
