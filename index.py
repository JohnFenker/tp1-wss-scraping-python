import urllib.request
from bs4 import BeautifulSoup
import json

datos = urllib.request.urlopen("http://www.cinemalaplata.com/").read().decode('latin1')

soup =  BeautifulSoup(datos)
tags = soup("img")
data = {}
data['peliculas'] = []
for tag in tags:
    data['peliculas'].append({
        'name_film': tag.get("alt"),
    })
with open('data.json', 'w') as file:
    json.dump(data, file, indent=3)