import requests
from bs4 import BeautifulSoup

url = "https://yts.ag/"
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)

def linkGenerator():
	for tag in divtag:
		nameTag = tag.find_all("a",{'class':'browse-movie-title'})
		yearTag = tag.find_all("div", {'class':'browse-movie-year'})
	for i in range(8):
		if nameTag[i].string == downloadMovie:
			yearAdd = yearTag[i].string
			movieName = nameTag[i].string
			movieName = movieName.lower()
			movieName = movieName.replace(":","-")
			movieName = movieName.replace(" ","-")
			movieName = movieName.replace("--","-")
			newUrl = movieName + "-" + yearAdd
			break
		elif(i == 7):
			print "Input Error"
	return newUrl

divtag = soup.select("[class~=content-dark]")
for tag in divtag:
	nameTag = tag.find_all("a",{'class':'browse-movie-title'})
	ratingTag = tag.find_all("h4",{'class':'rating'})
	yearTag = tag.find_all("div", {'class':'browse-movie-year'})

	for i in range(8):
		print "Movie Title:", nameTag[i].string
		print "IMDB Rating:", ratingTag[i].string
		print "Year of release:", yearTag[i].string
		print "*" * 20

choice = raw_input("Do you want the link of any of the above movies?(Y/N)\n>>> ")
choice = choice.lower()
if(choice == 'y'):
	downloadMovie = raw_input("Enter the name of the movie from the above movies whose link is required: \n>>> ")
	for tag in divtag:
		linkTag = tag.find_all("a",{'rel':'nofollow'},text='720p')
		for i in range(8):
			if(nameTag[i].string == downloadMovie):
				print
				print linkTag[i].get('href')


newUrl = linkGenerator()
newUrl = "https://yts.ag/movie/" + newUrl

newResponse = requests.get(newUrl)
newHtml = newResponse.content
newSoup = BeautifulSoup(newHtml)

SynopsisTag = newSoup.select("#synopsis")
for tag in SynopsisTag:
	synopsis = tag.find("p",{'class':'hidden-md'})
	print "\nSynopsis:\n" + synopsis.string
