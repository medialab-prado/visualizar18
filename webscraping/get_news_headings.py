from bs4 import BeautifulSoup
import requests

req  = requests.get("https://www.larazon.es/")
data = req.text
soup = BeautifulSoup(data, "html.parser")

query = 'a.lnknoticia'

result = soup.select(query)
for row in result:
    print(row['href'])
