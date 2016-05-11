import requests
from bs4 import BeautifulSoup

"""
Fetching of home url.
"""

url = "https://yts.ag/"
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)

"""
The function generates the url of the movie whose synopsis is to be
found by the user. Exception cases are handled and an input error is displayed
if the name entered by the user does not exist in the recent movie list.
"""

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
			movieName = movieName.replace("'","")
			movieName = movieName.replace(" ","-")
			movieName = movieName.replace("--","-")
			newUrl = movieName + "-" + yearAdd
			break
		elif(i == 7):
			print "Input Error"
	return newUrl

"""
Loop to get the movie name, IMDB rating, Year of Release from
the recent movies section.
"""

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

"""
The user enters the name of the movie whose torrent link is required.
The loop iterates over the anchor tags and returns the link.
"""

choice = raw_input("Do you want the link of any of the above movies?(Y/N)\n>>> ")
choice = choice.lower()
if(choice == 'y'):
	downloadMovie = raw_input("Enter the (exact)name of the movie from the above movies whose link is required: \n>>> ")
	for tag in divtag:
		linkTag = tag.find_all("a",{'rel':'nofollow'},text='720p')
		for i in range(8):
			if(nameTag[i].string == downloadMovie):
				print
				print linkTag[i].get('href')

"""
Parsing of the new url for synopsis generation.
The loop then extracts the synopsis of the movie from the 
movie's dedicated page.
"""

newUrl = linkGenerator()
newUrl = "https://yts.ag/movie/" + newUrl

newResponse = requests.get(newUrl)
newHtml = newResponse.content
newSoup = BeautifulSoup(newHtml)

SynopsisTag = newSoup.select("#synopsis")
for tag in SynopsisTag:
	synopsis = tag.find("p",{'class':'hidden-md'})
	print "\nSynopsis:\n" + synopsis.string

"""
Want to suggest something??
Raise an issue or submit a PR.
That will be all folks!!
"""