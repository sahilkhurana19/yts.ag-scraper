import requests
from bs4 import BeautifulSoup

url = "https://yts.ag/"
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)

divtag = soup.select("[class~=content-dark]")
for tag in divtag:
	nameTag = tag.find_all("a",{'class':'browse-movie-title'})
	ratingTag = tag.find_all("h4",{'class':'rating'})
	yearTag = tag.find_all("div", {'class':'browse-movie-year'})

	for i in range(8):
		print nameTag[i].string, "	" * 3,
		print ratingTag[i].string, "	" * 4,
		print yearTag[i].string