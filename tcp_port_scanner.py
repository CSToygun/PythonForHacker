#                _          _   _             _                                
#   ___ ___   __| | ___  __| | | |__  _   _  | |_ ___  _   _  __ _ _   _ _ __  
#  / __/ _ \ / _` |/ _ \/ _` | | '_ \| | | | | __/ _ \| | | |/ _` | | | | '_ \ 
# | (_| (_) | (_| |  __/ (_| | | |_) | |_| | | || (_) | |_| | (_| | |_| | | | |
#  \___\___/ \__,_|\___|\__,_| |_.__/ \__, |  \__\___/ \__, |\__, |\__,_|_| |_|
#                                     |___/            |___/ |___/  

import socket
from datetime import datetime
import requests

remoteServer = input("Adresi Giriniz :")
timeout = 2
remoteServer_IP_Adress = socket.gethostbyname(remoteServer)
print("Hedef :" + remoteServer_IP_Adress , "TimeoutDegeri : " + str(timeout))
a = input("Taranacak port baslangıc aralıgını giriniz ")
b = input("Taranacak port bitis aralıgını giriniz ")
zaman_1=datetime.now()

try:
    for port in range(int(a),(int(b)+1)) :
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((remoteServer_IP_Adress,port))
        if result == 0 :
            print("Port : "+str(port), "ACIK")
        else:
            print("Port : "+str(port),"KAPALI")

except Exception as erorr:
    print(str(erorr))

zaman_2=datetime.now()
toplam_sure= zaman_2 - zaman_1
print("Gecen Sure : "+ str(toplam_sure))
sock.close()

                _          _   _             _                                
   ___ ___   __| | ___  __| | | |__  _   _  | |_ ___  _   _  __ _ _   _ _ __  
  / __/ _ \ / _` |/ _ \/ _` | | '_ \| | | | | __/ _ \| | | |/ _` | | | | '_ \ 
 | (_| (_) | (_| |  __/ (_| | | |_) | |_| | | || (_) | |_| | (_| | |_| | | | |
  \___\___/ \__,_|\___|\__,_| |_.__/ \__, |  \__\___/ \__, |\__, |\__,_|_| |_|
                                     |___/            |___/ |___/  