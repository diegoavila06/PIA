import argparse
from scraping import scrapimage, scraplinks
from CorreosPIA import envcorreo
from Escaneo import Escaneo
from Encabezados import EscaneoHeaders
from Cifrado import CifradoC

def main():
    parser = argparse.ArgumentParser("Actividades de Ciberseguridad")
    parser.add_argument("-url", dest="url", help="Pagina a scrapear")
    parser.add_argument("-destinatario", dest="dest", help="Hacia quien esta dirigido"
    "el correo")
    parser.add_argument("-tema", dest="subject", help="Escriba el titulo")
    parser.add_argument("-cuerpo", dest="body", help="Esccribe el cuerpo del correo")
    parser.add_argument("-archivo", dest="arch", help="Nombre y extencion del archivo")
    parser.add_argument("-busqueda", dest="buscar", help="Indica que quiere buscar."
    " Ingresar solo un argumento",type=str)
    parser.add_argument("-ip", dest="direc", help="Indica tu ip remota")
    parser.add_argument("-ports", dest="ports", help="Indica el puerto(s) que quieras"
    " consultar separandolos con una coma Ejemplo:20,21,22")
    parser.add_argument("-mensaje", dest="msg", help="Mensaje a utilizar")
    parser.add_argument("-clave", dest="clv", help="Clave para cifrar")
    parser.add_argument("-accion", dest="act", help="Accion a realizar: Escaneo de puertos"
    "(p), Envio de correos(c), Webscraping(w), Busqueda de encabezados(e), Cifrar msg(m)")                    

    params = parser.parse_args()
    url = params.url
    receiver_email = params.dest
    subject = params.subject
    body = params.body
    filename = params.arch
    busqueda = params.buscar
    ip = params.direc
    puerto = params.ports
    message = params.msg
    clave = params.clv
    accion = params.act

    if (accion == "p"):
        puertos =params.ports.split(',')
        for i in range (len(puertos)):
            puertos[i] =int(puertos[i])
        Escaneo(ip, puertos)
                
    elif (accion == "c"):
        envcorreo(receiver_email,subject,body,filename)

    elif (accion == "w"):
        scrapimage(url)
        scraplinks(url)

    elif (accion == "e"):
        EscaneoHeaders(busqueda) 

    elif (accion == "m"):
        CifradoC(message, clave)

    else:
        print("Tienes que elgir un accion valida, Ejemplo: -accion p")
        exit()
if __name__=="__main__":
    main()



