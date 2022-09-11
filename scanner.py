#!/usr/bin/python3

import sys
import socket

def portScan(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    ret = s.connect_ex((ip, port))
    return ret

def main():
    list = []
    ip = socket.gethostbyname(sys.argv[1]) 
    for i in range(1, 65535):
        if not (portScan(ip, i)):
            list.append(i)
    for x in list:
        print("The port", x, "is opened")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Closed program")
        sys.exit()
    except socket.error:
        print("Timeout, impossible to connect")
        sys.exit()
