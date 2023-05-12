import os
import socket
import time

import pywifi


def disconnect_wifi():
    wifi = pywifi.PyWiFi()  # 创建一个PyWiFi对象
    iface = wifi.interfaces()[0]  # 获取第一个无线网卡接口
    iface.disconnect()  # 断开无线网络连接

def check_network():
    try:
        # Connect to Google's public DNS server to check for internet connectivity
        host = socket.gethostbyname("www.baidu.com")
        socket.create_connection((host, 80), 2)
        return True
    except:
        pass
    return False

while True:
    network_connected = False
    start_time = time.time()
    continuous_failed_count = 0  # 连续检测到网络连接失败的次数
    max_failed_count = 5*60 / 5  # 在5*60秒内最多允许失败的次数

    while (time.time() - start_time) < 30 * 60:
        time.sleep(5)
        if check_network():
            network_connected = True
            continuous_failed_count = 0
            break
        else:
            continuous_failed_count += 1
            print("Checking network connection...")
            if continuous_failed_count >= max_failed_count:
                print("No network connection for too long. Disconnecting Wi-Fi...")
                disconnect_wifi()
                break

    if network_connected:
        print("Network connected, starting next iteration.")
    else:
        print("Network not connected, restarting computer.")
        os.system("shutdown /r /t 1")