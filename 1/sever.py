#coding: utf-8

import socket

host = ''
port = 51423

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #setsockopt(level,optname,value)，SOL_SOCKET:希望使用socket协议，SO_REUSERADDR：socket关闭后该端口能马上重新使用，1：设置optname（这里即SO_REUSERADDR）为True
s.bind((host, port))
s.listen(1)

print "Server is running on port : %d" %port

while 1:
    clientsock, clientaddr = s.accept()
    clientfile = clientsock.makefile('rw', 0)
    clientfile.write('Welcome, ' + str(clientaddr) + "\n")
    clientfile.write("Please enter a string: ")
    line = clientfile.readline().strip()
    clientfile.write("You entered %d characters.\n" %len(line))
    clientfile.close()
    clientsock.close()
