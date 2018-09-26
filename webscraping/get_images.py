from lxml.html.soupparser import fromstring
from lxml.etree import tostring
import requests
import wget

url = "https://es.wikipedia.org/wiki/Alhambra"
query = ".//img/@src"

req  = requests.get(url)
root = fromstring(req.text)

for e in root.xpath(query):
    try:
        wget.download('http:'+e)
    except:
        pass
