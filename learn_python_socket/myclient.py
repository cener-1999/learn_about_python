# -*- coding: UTF-8 -*-

import socket

myclient=socket.socket()

myclient.connect(('localhost',1890))

myclient.send('hello,myserver!\n')

myclient.send('I`m myclient！')

while True:
    data=myclient.recv(1024)
    print("I heard what you have say\n")
    print(data)
    
myclient.close()