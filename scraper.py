import requests
from bs4 import BeautifulSoup

url = "https://yts.ag/"
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
print soup.prettify()