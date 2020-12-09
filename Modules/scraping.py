import logging
import re
import sys
import os,time,random
from urllib.request import Request, urlopen
import requests
import json

LOG_FORMAT = "%(asctime)s - %(message)s"
logging.basicConfig(filename = "./RegistroExcepciones.log", level = logging.DEBUG, format = LOG_FORMAT, filemode = 'w')
logger = logging.getLogger()

try:
    from bs4 import BeautifulSoup
except ImportError:
    logging.debug("No estan instalados los requerimentos")
    print("Instalando BeautifulSoup...")
    os.system('pip install bs4')
    exit()

def scrapimage(url):
    try:
        html = urlopen(url)
        bs = BeautifulSoup(html, 'html.parser')
        images = bs.find_all('img', {'src':re.compile('.jpg')})
        k= open("Images.txt", "a")
        k.write("Imagenes de la pagina:")
        for image in images: 
            k.write(image['src']+'\n')
        print("Se ha generado una lista de imagenes en Images.txt")
    except Exception as e:
        logging.debug("No se ha podido conectar a la url")
        print("La url no es valida  o no se ha podido conectar a ella")
        pass

def scraplinks(url):
    try:
        req = Request(url)
        html_page = urlopen(req)
        soup = BeautifulSoup(html_page, "lxml")
        links = []
        for link in soup.findAll('a'):
            links.append(link.get('href'))
        f= open("Links.txt", "a")
        f.write("Links de la pagina:\n")
        for item in links:
            f.write("%s\n" % item)
        print("Se ha generado una lista de links en Links.txt")
        indicators = links
        api_key='5075cc54d875f160201bd274d461ad8f6defca9081aeb2859d098e93e8cc9467'
        url = 'https://www.virustotal.com/vtapi/v2/url/report'
        for site in indicators:
            params = {'apikey': api_key, 'resource':site}
            response = requests.get(url, params=params)
            h = open ("Apireport.txt", "a")
            h.write(str(response.json()))
        print("Se han escaneado todas las url, se ha generado un reporte Apireport.txt")

    except Exception as e:
        logging.debug("No se ha podido conectar a la url")
        print("La url no es valida o no se ha podido conectar a ella")
        pass


