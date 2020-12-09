import os,time,random
import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import getpass
import logging

LOG_FORMAT = "%(asctime)s - %(message)s"
logging.basicConfig(filename = "./RegistroExcepciones.log", level = logging.DEBUG,
                    format = LOG_FORMAT, filemode = 'w')
logger = logging.getLogger()

try:
    import sys
except ImportError:
    logging.error("No estan instalados los requerimentos")
    print("Instalando Sys")
    os.system('pip install os-sys')
    exit()


def envcorreo(receiver_email,subject,body,filename):
    sender_email = "probandocuentapgc99@gmail.com"
    password = ("145236632541aA")

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  

    message.attach(MIMEText(body, "plain"))
 
    try:
        with open(filename, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        encoders.encode_base64(part)

        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )

        
        message.attach(part)
    except TypeError:
        pass
    
    text = message.as_string()
    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)
            print("Listo revisa tu email ;)")
    except ImportError as e:
        logging.error("No se ha podido iniciar sesion a su correo")
        print("No se ha podido conectar a su correo")
        pass

    
