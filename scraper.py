import requests
from bs4 import BeautifulSoup

url = "https://yts.ag/"
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
tags = soup.find_all("a", class_='browse-movie-title')

for tag in tags:
	print tag 