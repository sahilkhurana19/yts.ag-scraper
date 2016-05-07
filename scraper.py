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
	"""print nameTag[1].string
	for tag in nameTag:
		print tag.string
	for tag in ratingTag:
		print tag.string
	
	
	#for tag in ratingTag:
	#	print tag.string"""

	for i in range(8):
		print nameTag[i].string,
		print ratingTag[i].string