import urllib.request
from bs4 import BeautifulSoup
datos = urllib.request.urlopen("http://www.cinemalaplata.com/").read().decode('latin1')

soup =  BeautifulSoup(datos)
tags = soup("img")
for tag in tags:
	print(tag.get("alt"))