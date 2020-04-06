from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome("C:\chromedriver_win32/chromedriver.exe")
driver.get("https://www.cinepolis.com.ar/proximos-estrenos")
bsObj = BeautifulSoup(driver.page_source,'html.parser')
data = bsObj.find_all("a", string=lambda x: x and "Ver" in x)
for link in data:
    
    s = link.get("href")
    print(s)