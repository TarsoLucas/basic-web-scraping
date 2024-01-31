#this is an insanely basic web scraping test

import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"} 
link = "https://www.google.com/search?q=cotacao+dolar"
request = requests.get(link, headers=headers)
site= BeautifulSoup(request.text, "html.parser")

#print(site.prettify())

#titulo = site.find("title")
#print(titulo)

#pesquisa = site.find_all("input")
#print(pesquisa[1])

#pesquisa2 = site.find("input", class_="gLFyf")
#print(pesquisa2["value"])

cotacao_dolar = site.find("span", class_="SwHCTb")
print(cotacao_dolar["data-value"])
print(cotacao_dolar.get_text())



