#coding: utf-8

import socket, sys

port = 70
host = sys.argv[1]
filename = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#AF_INET:ipv4地址, SOCK_STREAM:TCP/IP协议
s.connect((host, port))
s.sendall(filename + '\r\n')

while 1:
    buf = s.recv(2048)
    if not len(buf):
        break
    sys.stdout.write(buf)
