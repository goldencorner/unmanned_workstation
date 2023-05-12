# unmanned_workstation
on network disconnection, automatically reconnect wifi or reboot(when the former doesn't work)

# summary 
- chk_network_reboot.py makes reboot when network error last for half an hour
- wifi_connect.py keep trying connecting wifi if it's not connected

# usage(windows)
1. get yout wifi ssid and name, which can be found in setting, and replace corresponding codes
2. creat .bat file for script launch and throw it into startup file (recommended).
