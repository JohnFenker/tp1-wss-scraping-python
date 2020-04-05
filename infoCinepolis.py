from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

req = Request('https://www.cinepolis.com.ar/?utm_source=migration&utm_medium=redirect&utm_campaign=migration', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
bsObj = BeautifulSoup(webpage);

for link in bsObj.find_all('a'):
    print(link.get('href'))