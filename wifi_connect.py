import os
import time

# os.system("netsh wlan connect ssid=TJ-WIFI name=TJ-WIFI")
# time.sleep(3)
while 1:

    ret=os.system("netsh WLAN show interfaces | findStr TJ-WIFI >nul")
    if ret!=0:
        os.system("netsh wlan connect ssid=TJ-WIFI name=TJ-WIFI")
        time.sleep(3)

    time.sleep(3)
