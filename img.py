import bs4
import requests
import urllib.request
import os
def makesoup(url):
	thepage=requests.get(url)
	soupdata=bs4.BeautifulSoup(thepage.text,'lxml')
	return soupdata
soup=makesoup("https://www.pexels.com/")
def download(soupy):
	for img in soup.findAll("img"):
		image=img.get('srcset')
		nametemp=img.get('alt')
		if image is None:
			continue
		else:	
			if nametemp is None:
				continue
			else:
				r = requests.get(image, allow_redirects=True)
				open( nametemp + ".jpeg", 'wb').write(r.content)
download('soup')
print("All photos downloaded")
