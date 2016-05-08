import requests
from bs4 import BeautifulSoup

url = "https://yts.ag/"
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)

"""def linkGenerator():
		downloadMovie = raw_input("Enter the name of the movie from the above movies whose link is required: \n>>> ")
		for tag in divtag:
			nameTag = tag.find_all("a",{'class':'browse-movie-title'})
			yearTag = tag.find_all("div", {'class':'browse-movie-year'})
		for i in range(8):
			if nameTag[i].string == downloadMovie:
				yearAdd = yearTag[i].string
				print "Movie Found"
				movieName = nameTag[i].string
				movieName = movieName.lower()
				movieName = movieName.replace(" ","-")
				#search = 
				#searcher = "".join(letter for letter in movieName if letter.isalnum())
				#print searcher
				print movieName
				print yearAdd
				break
			elif(i == 7):
				print "Input Error"
"""


divtag = soup.select("[class~=content-dark]")
for tag in divtag:
	nameTag = tag.find_all("a",{'class':'browse-movie-title'})
	ratingTag = tag.find_all("h4",{'class':'rating'})
	yearTag = tag.find_all("div", {'class':'browse-movie-year'})

	for i in range(8):
		print nameTag[i].string, "	" * 3,
		print ratingTag[i].string, "	" * 4,
		print yearTag[i].string

choice = raw_input("Do you want the link of any of the above movies?(Y/N)\n>>> ")
choice = choice.lower()
#if(choice == 'y'):
#	linkGenerator()
#else:
#	print "That will be all folks."

if(choice == 'y'):
	downloadMovie = raw_input("Enter the name of the movie from the above movies whose link is required: \n>>> ")
	for tag in divtag:
		linkTag = tag.find_all("a",{'rel':'nofollow'},text='720p')
		for i in range(8):
			#print linkTag[i]
			if(nameTag[i].string == downloadMovie):
					print linkTag[i].get('href')
			