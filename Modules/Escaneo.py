import socket
import sys
import logging
import subprocess

LOG_FORMAT = "%(asctime)s - %(message)s"
logging.basicConfig(filename = "./RegistroExcepciones.log", level = logging.DEBUG,
                    format = LOG_FORMAT, filemode = 'w')
logger = logging.getLogger()
 
def Escaneo(ip,puertos):
    try:
        for port in puertos:
            sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            result = sock.connect_ex((ip,port))
        if result == 0:
            f= open("Puertos.txt", "a")
            f.write("\nPuerto {}:\t Abierto".format(port))
            f.close()
        else:
            f= open("Puertos.txt", "a")
            f.write("\nPuerto {}:\t Cerrado".format(port))
            f.close()
        sock.close()
        print("Se ha generado un reporte de los puertos en Puertos.txt")
        subprocess.call(r'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe Set-ExecutionPolicy -ExecutionPolicy Bypass', shell=True)
        p = subprocess.Popen([r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe", r"C:\Users\user\Downloads\Logs_PIA.ps1"], stdout=sys.stdout)
        p.communicate()
    except (OverflowError , UnboundLocalError) as error:
        logging.error("El argumento ingresado es erroneo")
        print("El argumento ingresado es erroneo")
        pass
    
        
    except socket.error as error:
        logging.error("Error en la conexion")
        print("Error en la conexion")
        sys.exit()
        pass


