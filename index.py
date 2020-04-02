import urllib.request
from bs4 import BeautifulSoup
import json

#metodo que recupera informacion de una pelicula y devuelve en forma de JSON
def getInfoFilm(IdTitulo):
    urlStr = "http://www.cinemalaplata.com/sinopsis.aspx?Seccion=FUTURO&IdTitulo=" + IdTitulo
    datos = urllib.request.urlopen(urlStr).read().decode('latin1')
    soup =  BeautifulSoup(datos)
    titulos = soup.find_all("h4", {"class": "shortcodes-title"})
    for titulo in titulos:
        print(titulo.text.strip())

def main():
    datos = urllib.request.urlopen("http://www.cinemalaplata.com/").read().decode('latin1')

    soup =  BeautifulSoup(datos)
    tags = soup.find_all("div", {"class": "item1"})

    for tag in tags:
        var = tag.find(["a"])
        s = var.get("href")
        start = 'IdTitulo='
        end = 'false'
        inicio = s.split("IdTitulo=", 1)
        var = 1
        for ss in inicio:
           if var == 2:
                final = ss.split(",", 1)
                url = ((final[0])[:-1])
                getInfoFilm(url)
           var=var+1
     


if __name__ == '__main__':
    main()

