# pip install beautifulsoup4
# pip install lxml
from bs4 import BeautifulSoup
import requests

contador = 0
consulta = "YouTube"
num = 10
headers = {'User-Agent':'Mozilla/5.0 (X11: Linux x86_64; rv::12.0) Gecko/20100101 Firefox/21.0'}
while True:
    parametros = {'q': consulta, 'start':contador,'num':num}
    resposta = requests.get('http://www.google.com.br/search', \
                            params = parametros, timeout = 2, headers=headers)
    msg = "Our systems have detected unsual traffic from your computer network"
    if msg in resposta.text:
        print "O Google detectou o comportamento do bot..."
        break
    bs = BeautifulSoup(resposta.text,"lxml")
    cites = bs.find_all("cite")
    if len(cites) ==0:
        break
    divs = bs.find_all("div", {"class":"g"})
    print divs
    for div in divs:
        try:
            print div.h3.a.text
            print div.h2.r["href"]
            print div.find("span", {"class":"st"}).text
            print
        except Exception:
            pass
    contador += 10


# USE O SELENIUM