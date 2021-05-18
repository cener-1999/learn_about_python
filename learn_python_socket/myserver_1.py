import socket

servers=socket.socket()

servers_addr=('localhost',1999)

servers.bind(servers_addr)

servers.listen(3)


servers.send('if i can fly')
connect,clinet_addr=servers.accept()


data=connect.recv(1024)

print(data)

connect.close()
servers.close()

