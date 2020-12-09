import os,time,random
import sys
import logging

LOG_FORMAT = "%(asctime)s - %(message)s"
logging.basicConfig(filename = "./RegistroExcepciones.log", level = logging.DEBUG,
                    format = LOG_FORMAT, filemode = 'w')
logger = logging.getLogger()

try:
    from googlesearch import search
except ImportError:
    logging.error("No estan instalados los requerimentos")
    print("Instalando google...")
    os.system('pip install google')
    exit()
    
try:
    import requests
except ModuleNotFoundError:
    logging.error("No estan instalados los requerimentos")
    print("Instalando requests")
    os.system('pip install requests')
    exit()

def EscaneoHeaders(busqueda):
    x=1
    query = busqueda
    for enlace in search(query,tld="com",num=10,stop=11,pause=5):
        r = requests.get(enlace)
        headers=r.headers
        f= open("Encabezados.txt", "a")
        f.write((str(x))+":"+(str(headers))+"\n")
        x=x+1
        f.close()
    print("Se ha generado una lista de encabezados en el archivo Encabezados.txt")

       


    
