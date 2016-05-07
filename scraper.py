import requests
from bs4 import BeautifulSoup

url = "https://yts.ag/"
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)

divtag = soup.select("[class~=content-dark]")
for tag in divtag:
	aTag = tag.find_all("a",{'class':'browse-movie-title'})
	for tag in aTag:
		print tag.string