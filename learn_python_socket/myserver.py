# -*- coding: UTF-8 -*-
import socket

server_addr=('127.0.0.1',1890)#写错了

myserver=socket.socket()
myserver.bind(server_addr)

myserver.listen(10)

#welcome='my first server tsets'
#myserver.send("welcome")


while True:

    connetion,client_addr=myserver.accept()
    connetion.send('welcome')
    get_data=connetion.recv(1024)
    print("client said:",get_data)
    
connetion.close()
myserver.close()

'''
一个错误，server.accept()接收的不是客户端的嵌套字，而是新建立了一个    嵌套字，服务器通过它和客户端通信
    Q；那多线程呢？群聊呢？服务器通过多个socket交流吗？


    myclient,client_addr=myserver.accept()
    get_data=myclient.recv(1024)
'''

