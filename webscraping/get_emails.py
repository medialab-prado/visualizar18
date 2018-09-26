from lxml.html.soupparser import fromstring
from lxml.etree import tostring
import requests
import wget

url = "https://www.larazon.es/nav_general/quienes-somos"
query = ".//a[contains(@href,'mailto')]"

req  = requests.get(url)
root = fromstring(req.text)

for e in root.xpath(query):
    print(e.text)
