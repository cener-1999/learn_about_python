# -*- coding: UTF-8 -*-

import socket                   #导入包

s=socket.socket()               #创建socket
host=socket.gethostname()       #获取主机名
port=12345                      #设置端口
s.bind(("localhost",port))             #绑定端口

s.listen(5)                     #等待客户端连接

while True:
    c,addr=s.accept()           #建立客户端连接
    print ("连接地址：",addr)
    c.send('欢迎访问,问问问')
    c.close()