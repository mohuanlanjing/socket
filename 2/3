#coding: utf-8

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #使用ipv4和tcp

print 'Looking up port number...'
port = socket.getservbyname('http', 'tcp')

print 'Connecting to remote host on port %d...'%port
s.connect(('www.baidu.com', port))
