import json

archivo = open("dataCinema.json")
datos = archivo.read().encode('utf-8')
info = json.loads(datos)

pelis = info['peliculas']
for peli in pelis:
    generos = peli['G\u00e9nero']
    res = [i for i in generos if 'Ciencia' in i]
    if len(res)>0:
        print(peli['Titulo'] + ' pertenece a al genero CIENCIA FICCION')

     