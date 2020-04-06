import urllib.request
from bs4 import BeautifulSoup
import json

#metodo que recupera informacion de una pelicula y devuelve en forma de JSON
def getInfoFilm(IdTitulo, data):
    urlStr = "http://www.cinemalaplata.com/sinopsis.aspx?Seccion=FUTURO&IdTitulo=" + IdTitulo
    datos = urllib.request.urlopen(urlStr).read().decode('latin1')
    soup =  BeautifulSoup(datos)

    nombrePelicula = soup.find("div", {"class": "post-container page-title"})
    diccionario = {}
    diccionario["Titulo"] = nombrePelicula.text.strip()
    detallesDePelicula = soup.find_all("div", {"class": "dropcap6"})
    for detalle in detallesDePelicula:
        nombreCampo = detalle.find("h4")
        valorCampo = detalle.find("span")
        listaValores=valorCampo.text.strip()
        datos = listaValores.split(",")
        diccionario[nombreCampo.text.strip()] = datos
    #agrego el diccionario a un objeto del param data json
    data['peliculas'].append(diccionario)
    

def main():
    data = {}
    data['peliculas'] = []
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
                getInfoFilm(url, data)
           var=var+1
    with open('dataCinema.json', 'w') as file:
        json.dump(data, file, indent=3)
     


if __name__ == '__main__':
    main()

